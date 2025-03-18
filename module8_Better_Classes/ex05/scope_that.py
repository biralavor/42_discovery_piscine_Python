#!/usr/bin/python3.12

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 12:30:17 by umeneses          #+#    #+#              #
#    Updated: 2025/03/11 12:30:18 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class scopeThat:
  def __init__(self, user_input):
    self.user_input = user_input

  def input_catcher(self):
    user_input = input("Enter a number (I'll increment it using 'classes'): ")
    return user_input

  def input_validation(self):
    while True:
      nbr = self.input_catcher()
      try:
        nbr = (int(nbr))
        break
      except ValueError:
        sys.stderr.write(f"'{nbr}' wasn't a number. Try again!\n")
    return nbr

  def increment_one(self, nbr):
    nbr += 1
    return nbr
  
  def scope_init(self, user_input):
    result = self.increment_one(user_input)
    return result

if __name__ == "__main__":
  arg_input = scopeThat("")
  nbr = arg_input.input_validation()
  result = arg_input.scope_init(nbr)
  print(f"Here was your original value >>>>> {nbr}")
  print(f"Here is the incremented result >>> {result}")
