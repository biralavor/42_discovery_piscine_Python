#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 10:08:15 by umeneses          #+#    #+#              #
#    Updated: 2025/02/25 10:08:16 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ask_number(nbr) :
  return (int(input(f'Give me the {nbr} number: ')))

def calculator(operation, first_nbr, second_nbr) :
  if operation == 1 :
    return first_nbr + second_nbr
  elif operation == 2 :
    return first_nbr - second_nbr
  elif operation == 3 :
    return first_nbr // second_nbr
  elif operation == 4 :
    return first_nbr * second_nbr

def sign_definition(operation) :
  if operation == 1 :
    return '+'
  elif operation == 2 :
    return '-'
  elif operation == 3 :
    return '/'
  elif operation == 4 :
    return '*'

if __name__ == "__main__":
  first_nbr = ask_number('first')
  second_nbr = ask_number('second')
  print('Thank you!')
  for operation in range (1, 5) :
    sign = sign_definition(operation)
    result = calculator(operation, first_nbr, second_nbr)
    print(f'{first_nbr} {sign} {second_nbr} = {result}')
