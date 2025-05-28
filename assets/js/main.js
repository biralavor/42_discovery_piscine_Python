// main.js - Terminal logic for Python Studies
const studyFiles = [
  "module8_Better_Classes/ex03/greetings_for_all.py",
  "module8_Better_Classes/ex01/upcase_it.py",
  "module8_Better_Classes/ex05/scope_that.py",
  "module4_Simple_Methods/ex01/age.py",
  "module3_Better_Input_Validation/ex01/multiplication_table.py",
  "module3_Better_Input_Validation/ex02/i_got_that.py",
  "module8_Better_Classes/ex04/methods_everywhere.py"
];
const baseURL = "https://biralavor.github.io/42_discovery_piscine_Python";
let pyodideLoaded = false;
let terminalState = "intro"; // intro, menu, running, output
let selectedFileIdx = 0;

// Pre-generated briefs for each study file
const studyFileBriefs = {
  "module8_Better_Classes/ex03/greetings_for_all.py": "Prints personalized greetings for all users in a list using classes.",
  "module8_Better_Classes/ex01/upcase_it.py": "Converts input strings to uppercase using a class method.",
  "module8_Better_Classes/ex05/scope_that.py": "Demonstrates variable scope and class/instance attributes.",
  "module4_Simple_Methods/ex01/age.py": "Calculates and displays age based on user input.",
  "module3_Better_Input_Validation/ex01/multiplication_table.py": "Prints a multiplication table for a given number with input validation.",
  "module3_Better_Input_Validation/ex02/i_got_that.py": "Checks if a user-provided value exists in a predefined list.",
  "module8_Better_Classes/ex04/methods_everywhere.py": "Shows how to use methods in different class contexts."
};

function ansiTitle() {
  return `\u001b[1;32m
             _   _                       _             _ _           
            | | | |                     | |           | (_)          
 _ __  _   _| |_| |__   ___  _ __    ___| |_ _   _  __| |_  ___  ___ 
| '_ \\| | | | __| '_ \\ / _ \\| '_ \\  / __| __| | | |/ _\` | |/ _ \\/ __|
| |_) | |_| | |_| | | | (_) | | | | \\__ \\ |_| |_| | (_| | |  __/\\__ \\
| .__/ \\__, |\\__|_| |_|\\___/|_| |_| |___/\\__|\\__,_|\\__,_|_|\\___||___/
| |     __/ |                                                        
|_|    |___/                                                         

\n\u001b[0m`;
}

function introText() {
  return `Welcome to Python Studies!\n\nThis is a live terminal playground for Python, powered by Pyodide.\n\nAuthor: Bira Lavor (https://github.com/biralavor)\n`;
}

function menuText() {
  let menu = "Choose a study file to run (use arrow keys and press Enter):\n";
  studyFiles.forEach((file, idx) => {
    menu += (idx === selectedFileIdx ? "> " : "  ") + file + "\n";
  });
  // Add the brief for the currently selected file
  const brief = studyFileBriefs[studyFiles[selectedFileIdx]] || "No description available.";
  menu += "\nStudy file brief:\n" + brief;
  return menu;
}

function printToTerminal(text, isAnsi = false) {
  const output = document.getElementById("terminal-output");
  if (isAnsi) {
    output.innerHTML = ansiToHtml(text);
  } else {
    output.textContent = text;
  }
}

function ansiToHtml(text) {
  // Simple ANSI color to HTML (green/yellow/blue)
  return text
    .replace(/\u001b\[1;32m/g, '<span style="color:#00ff5f;font-weight:bold">')
    .replace(/\u001b\[0m/g, '</span>')
    .replace(/\n/g, '<br>');
}

function showIntro() {
  // Render ANSI title in the header
  document.querySelector(".terminal-header").innerHTML = ansiToHtml(ansiTitle());
  printToTerminal(introText(), false);
  document.getElementById("terminal-input").style.display = "none";
  document.getElementById("run-pyodide-btn").style.display = "inline-block";
  terminalState = "intro";
}

function showMenu() {
  printToTerminal(menuText());
  document.getElementById("terminal-input").style.display = "none";
  terminalState = "menu";
}

function showPrompt() {
  document.getElementById("terminal-input").style.display = "block";
  document.getElementById("terminal-input").focus();
}

function showOutput(text) {
  printToTerminal(text + "\n\n[Right Arrow →] Check source code  |  [b] Back to menu");
  terminalState = "output";
  showPrompt();
  // Show mobile button for source code
  const btn = document.getElementById("show-source-btn");
  if (btn) btn.style.display = "inline-block";
}

async function showSourceCode() {
  const file = studyFiles[selectedFileIdx];
  printToTerminal("Loading source code for: " + file + "...\n");
  try {
    const response = await fetch(baseURL + "/" + file);
    if (!response.ok) throw new Error("File not found");
    const code = await response.text();
    printToTerminal(
      `Source code for: ${file}\n\n` + code +
      "\n\n[←] Back to output  |  [b] Back to menu"
    );
    terminalState = "source";
    // Hide mobile button
    const btn = document.getElementById("show-source-btn");
    if (btn) btn.style.display = "none";
  } catch (err) {
    printToTerminal("Error loading source: " + err);
    terminalState = "output";
  }
}

function listenForMenuKeys() {
  document.addEventListener('keydown', function(e) {
    if (terminalState === "menu") {
      if (e.key === "ArrowUp") {
        selectedFileIdx = (selectedFileIdx - 1 + studyFiles.length) % studyFiles.length;
        showMenu();
      } else if (e.key === "ArrowDown") {
        selectedFileIdx = (selectedFileIdx + 1) % studyFiles.length;
        showMenu();
      } else if (e.key === "Enter") {
        runSelectedStudyFile();
      }
    } else if (terminalState === "output") {
      if (e.key === "ArrowRight") {
        showSourceCode();
      } else if (e.key.toLowerCase() === "b") {
        showMenu();
        // Hide mobile button
        const btn = document.getElementById("show-source-btn");
        if (btn) btn.style.display = "none";
      }
    } else if (terminalState === "source") {
      if (e.key === "ArrowLeft") {
        // Go back to output
        showOutput(lastOutputText);
      } else if (e.key.toLowerCase() === "b") {
        showMenu();
      }
    }
  });
}

// Store last output for back navigation from source view
let lastOutputText = "";

async function runSelectedStudyFile() {
  terminalState = "running";
  printToTerminal("Running: " + studyFiles[selectedFileIdx] + "...\n");
  try {
    await pyodide.runPythonAsync(`import sys\nfrom io import StringIO\nsys.stdout = StringIO()`);
    const response = await fetch(baseURL + "/" + studyFiles[selectedFileIdx]);
    if (!response.ok) throw new Error("File not found");
    const code = await response.text();
    await pyodide.runPythonAsync(code);
    let output = await pyodide.runPythonAsync("sys.stdout.getvalue()");
    lastOutputText = output || "(No output)";
    showOutput(lastOutputText);
  } catch (err) {
    lastOutputText = "Error: " + err;
    showOutput(lastOutputText);
  }
}

async function runPyodide() {
  document.getElementById("run-pyodide-btn").textContent = "Loading Pyodide...";
  window.pyodide = await loadPyodide();
  pyodideLoaded = true;
  document.getElementById("run-pyodide-btn").style.display = "none";
  showMenu();
  listenForMenuKeys();
}
window.runPyodide = runPyodide;

// Add a button for mobile users to check source code
window.addEventListener("DOMContentLoaded", function() {
  const btn = document.createElement("button");
  btn.id = "show-source-btn";
  btn.textContent = "Check Source Code";
  btn.style.display = "none";
  btn.className = "terminal-btn";
  btn.onclick = showSourceCode;
  document.querySelector(".terminal-body").appendChild(btn);
});

document.addEventListener("DOMContentLoaded", showIntro);
