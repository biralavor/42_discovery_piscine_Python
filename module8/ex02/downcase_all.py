#!/usr/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 13:07:06 by umeneses          #+#    #+#              #
#    Updated: 2025/03/10 13:07:07 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class ModifyAscii:
  def __init__(self, parameters):
    self.parameters = parameters
  
  def param_catcher(self):
    outside_params = []
    for param in range (1, len(sys.argv)):
      outside_params.append(sys.argv[param])
    return outside_params

  def upcase_it(self):
    for param in range(0, len(self.parameters)):
      self.parameters[param] = self.parameters[param].upper()
    return self.parameters
  
  def downcase_it(self):
    for param in range(0, len(self.parameters)):
      self.parameters[param] = self.parameters[param].lower()
    return self.parameters

if __name__ == "__main__":
  outside_param = ModifyAscii("")
  saved_params = outside_param.param_catcher()
  print(f"Here is the input  >>> {saved_params}")
  object_tobe_modified = ModifyAscii(saved_params)
  result = object_tobe_modified.downcase_it()
  print(f"Here is the result >>> {result}")
