#!/usr/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 12:03:51 by umeneses          #+#    #+#              #
#    Updated: 2025/03/10 12:03:52 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class ModifyAscii:
  def __init__(self, name):
    self.name = name
  
  def input_catcher(self):
    user_input = input("Please enter a string: ")
    return user_input

  def upcase_it(self):
    self.name = self.name.upper()
    return self.name

if __name__ == "__main__":
  user_input = ModifyAscii("")
  name = user_input.input_catcher()
  object_tobe_modified = ModifyAscii(name)
  result = object_tobe_modified.upcase_it()
  print(f"Here is the result >>> {result}")
