#!/usr/bin/python3.8

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

while True :
  users_nbr = input('Enter a number: ')
  try :
    users_nbr = int(users_nbr)
    break
  except ValueError :
    print("Your input wasn't a number. Try again!")
for idx in range(0, 10) :
  result = users_nbr * idx
  print(f'{idx} x {users_nbr} = {result}')
  idx += 1
exit()