#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 14:27:25 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 14:27:26 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

while True :
  users_nbr = input('Enter a number less than 25: ')
  try :
    users_nbr = int(users_nbr)
    if users_nbr > 25 :
      sys.stderr.write('Error\n')
    else :
      while users_nbr <= 25 :
        print(f'Inside the loop, my variable is {users_nbr}')
        users_nbr += 1
      break
  except ValueError :
    print("Your input wasn't a number. Try it again.")