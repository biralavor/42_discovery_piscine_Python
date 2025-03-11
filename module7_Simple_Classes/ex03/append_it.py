#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    append_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/28 12:59:24 by umeneses          #+#    #+#              #
#    Updated: 2025/02/28 12:59:25 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

class  AppendThis :
  def __init__(self, outside_param, toappend) :
    self.outside_param = outside_param
    self.toappend = toappend
  
  def first_argv_remover(self) :
    self.outside_param.pop(0)
    return self.outside_param
  
  def toappend_occurencies_searcher(self, idx) :
    if re.search(self.toappend, self.outside_param[idx]) :
      return True
    return False
  
  def list_updater(self, old_list) :
    idx = 0
    while idx < len(old_list) :
      if self.toappend_occurencies_searcher(idx) :
        old_list.pop(idx)
      else :
        old_list[idx] += self.toappend
        idx += 1
    return old_list
  
  def list_printer(self) :
    for arg in self.outside_param :
      print(arg)

  def append_this_runner(self) :
    old_list = self.first_argv_remover()
    _ = self.list_updater(old_list)
    self.list_printer()

if __name__ == "__main__" :
  if len(sys.argv) > 1 :
    outside_param = sys.argv
    toappend = "ism"
    class_runner = AppendThis(outside_param, toappend)
    class_runner.append_this_runner()
  else :
    print('none')

