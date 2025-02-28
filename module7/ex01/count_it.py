#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 16:09:33 by umeneses          #+#    #+#              #
#    Updated: 2025/02/27 16:09:34 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class ParamCounter :
  def __init__(self, parameters, total_params, argv_len) :
    self.parameters = parameters
    self.total_params = total_params
    self.argv_len = argv_len
  
  def param_count(self) :
    self.total_params = len(self.parameters) - 1
  
  def param_list(self) :
    self.parameters.pop(0)                  # To remove the 1st argv
    # self.parameters = self.parameters[1:] # A new list without the 1st argv
    return self.parameters
  
  def printer(self) :
    param_list = self.param_list()
    print(f'parameters as a List: {param_list}')
    print(f'parameters total: {self.total_params}')
    for idx in range(0, self.total_params) :
      print(f'{self.parameters[idx]}: {len(self.parameters[idx])}')

if __name__ == "__main__" :
  if len(sys.argv) > 1 :
    outside_param = sys.argv
    counter_it = ParamCounter(outside_param, 0, 0)
    counter_it.param_count()
    counter_it.printer()
  else :
    print('none')