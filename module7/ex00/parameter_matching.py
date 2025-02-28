#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 11:27:17 by umeneses          #+#    #+#              #
#    Updated: 2025/02/27 11:27:19 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class ParamMatcher :
  def __init__(self, outside_param, input_param):
    self.input_param = input_param
    self.outside_param = outside_param

  def match(self):
    if self.input_param == self.outside_param:
      print('Good job!')
      return True
    else :
      print('Nope, sorry...')
      return False

if __name__ == "__main__" :
  if len(sys.argv) == 2 :
    outside_param = sys.argv[1]
    input_param = input("What was the parameter? ")
    parameter_matching = ParamMatcher(outside_param, input_param)
  while not parameter_matching.match() :
    input_param = input("What was the parameter? ")
    parameter_matching = ParamMatcher(outside_param, input_param)