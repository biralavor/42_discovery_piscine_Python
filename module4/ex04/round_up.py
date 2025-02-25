#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    round_up.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 11:50:27 by umeneses          #+#    #+#              #
#    Updated: 2025/02/25 11:50:29 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def round_up(users_nbr) :
  nbr = float(users_nbr)
  rounded_nbr = math.ceil(nbr)
  print(rounded_nbr)

def input_validation() :
  while True :
    users_nbr = input('Give me a number: ')
    if users_nbr.isnumeric() or users_nbr.replace('.', '', 1).isnumeric() :
      break
    else :
      print('Only numbers are allowed. Try it again!')
  return users_nbr

if __name__ == "__main__" :
  users_nbr = input_validation()
  round_up(users_nbr)