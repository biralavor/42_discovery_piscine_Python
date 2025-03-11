#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    up_low.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 11:56:21 by umeneses          #+#    #+#              #
#    Updated: 2025/02/25 11:56:22 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def swapcase(users_input) :
  converted_input = str.swapcase(users_input)
  print(converted_input)

def input_validation() :
  while True :
    users_input = input('Give me a word: ')
    try :
      users_input = str(users_input)
      break
    except ValueError :
      print('Only words are allowed. Try it again!')
  return users_input

if __name__ == "__main__" :
  users_input = input_validation()
  swapcase(users_input)