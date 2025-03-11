#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/28 10:51:15 by umeneses          #+#    #+#              #
#    Updated: 2025/02/28 10:53:41 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class SearchThisChar :
  def __init__(self, outside_param, tofind) :
    self.outside_param = outside_param
    self.tofind = tofind

  def first_argv_remover(self) :
    self.outside_param.pop(0)
    return self.outside_param

  def occurencies_searcher(self) :
    new_list = self.first_argv_remover()
    occurencies = 0
    for arg in new_list :
      occurencies += arg.count(self.tofind)
    return occurencies

  def n_occurencies_printer(self) :
    occurencies = self.occurencies_searcher()
    for _ in range(occurencies) :
      sys.stdout.write(self.tofind)
  
  def search_this_char_runner(self) :
    self.n_occurencies_printer()

if __name__ == "__main__" :
  if len(sys.argv) > 1 :
    outside_param = sys.argv
    tofind = 'z'
    class_runner = SearchThisChar(outside_param, tofind)
    class_runner.search_this_char_runner()
  else :
    print('none')