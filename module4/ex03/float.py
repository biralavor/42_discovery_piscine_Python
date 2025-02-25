#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 10:27:32 by umeneses          #+#    #+#              #
#    Updated: 2025/02/25 10:27:33 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_number_type(users_nbr) :
  converted_nbr = float(users_nbr)
  is_an_int = int(converted_nbr)
  if is_an_int == converted_nbr :
    print(f'The number {is_an_int} is an integer.')
  else :
    print(f'The number {converted_nbr} is a decimal.')

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
  check_number_type(users_nbr)