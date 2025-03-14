#!/usr/bin/python3.12

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
  def __init__(self, old_input):
    self.old_input = old_input
  
  def input_catcher(self):
    user_input = input("Please enter a string: ")
    return user_input

  def upcase_it(self):
    self.old_input = self.old_input.upper()
    return self.old_input

if __name__ == "__main__":
  user_input = ModifyAscii("")
  old_input = user_input.input_catcher()
  object_tobe_modified = ModifyAscii(old_input)
  result = object_tobe_modified.upcase_it()
  print(f"Here was your input >>> {old_input}")
  print(f"Here is the result  >>> {result}")
