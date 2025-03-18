#!/usr/bin/python3.12

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 15:01:17 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 15:01:18 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
class multiplicationTable:
  def __init__(self, user_input):
    self.user_input = user_input

  def input_catcher(self):
    user_input = input('Enter a number: ')
    return user_input

  def input_validation(self):
    while True :
      try :
        nbr = int(self.input_catcher())
        break
      except ValueError :
        sys.stderr.write("Your input wasn't a number. Try again!\n")
    return nbr

  def multiplyIt(self, nbr):
    for idx in range(0, 10) :
      result = nbr * idx
      print(f'{idx} x {nbr} = {result}')
      idx += 1

if __name__ == "__main__":
  arg_input = multiplicationTable("")
  nbr = arg_input.input_validation()
  print(f"Here is the Multiplication Table for {nbr}:")
  arg_input.multiplyIt(nbr)