#!/usr/bin/python3.7

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
    if isinstance(self.name, int):
      name = -2
    elif self.name == '':
      name = -1
    else:
      name = self.name
    return name

  def greetings(self):
    name = self.input_validation()
    if name == -2:
      print("Error! It was not a name.")
    elif name == -1:
      name = "noble stranger"
      print(f"Hello, {name}!")
    else:
      print(f"Hello, {name}!")

if __name__ == "__main__":
  name = GreetingsForAll("Alexandra")
  name.greetings()
  name = GreetingsForAll("Wil")
  name.greetings()
  name = GreetingsForAll("")
  name.greetings()
  name = GreetingsForAll(42)
  name.greetings()
