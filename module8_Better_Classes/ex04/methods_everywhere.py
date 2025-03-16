#!/usr/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 15:51:04 by umeneses          #+#    #+#              #
#    Updated: 2025/03/10 15:51:04 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class MethodsEverywhere:
  MAX = 8

  def __init__(self, outside_param):
    self.outside_param = outside_param

  def param_catcher(self):
    outside_param = []
    for idx in range(1, len(sys.argv)):
      outside_param.append(sys.argv[idx])
    return outside_param

  def shrink(self, one_param):
    sliced_limit = slice(0, MethodsEverywhere.MAX)
    sliced_param = one_param[sliced_limit]
    return sliced_param
  
  def enlarge(self, one_param):
    char_tobe_added = "z"
    for _ in range(len(one_param), MethodsEverywhere.MAX):
      one_param += char_tobe_added
    return one_param
  
  def automate_method(self):
    saved_params = self.param_catcher()
    for param in saved_params:
      if len(param) > MethodsEverywhere.MAX:
        result = self.shrink(param)
        print(f"SHRINKING this input >>> [{param}] to fit the limit of {MethodsEverywhere.MAX}")
        print(f"  Here is the result >>> {result}")
        print("/////////")
      else:
        result = self.enlarge(param)
        print(f"ENLARGING this input >>> [{param}] to fit the limit of {MethodsEverywhere.MAX}")
        print(f"  Here is the result >>> {result}")
        print("/////////")

if __name__ == "__main__":
  outside_param = MethodsEverywhere("")
  saved_params = outside_param.automate_method()
