#!/usr/bin/python3.12

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 13:34:49 by umeneses          #+#    #+#              #
#    Updated: 2025/03/10 13:34:50 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GreetingsForAll:
  def __init__(self, name):
    self.name = name

  def input_validation(self):

    try:
      int(self.name)
      is_int = True
    except ValueError:
      is_int = False
    # if isinstance(self.name, int):
    if is_int:
      name = -2
    elif self.name == '' and not is_int:
      name = -1
    else:
      name = self.name
    return name

  def greetings(self):
    name = self.input_validation()
    if name == -2:
      print("Sorry! This is not a name.")
    elif name == -1:
      name = "noble stranger"
      print(f"Hello, {name}!")
    else:
      print(f"Hello, {name}!")

if __name__ == "__main__":
  # name = GreetingsForAll("Alexandra")
  # name.greetings()
  # name = GreetingsForAll("Wil")
  # name.greetings()
  # name = GreetingsForAll("")
  # name.greetings()
  # name = GreetingsForAll(42)
  # name.greetings()
  user_input = input("What's your name? (You can also say a number or nothing) ")
  name = GreetingsForAll(user_input)
  name.greetings()
