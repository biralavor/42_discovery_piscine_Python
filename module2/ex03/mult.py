#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 14:17:28 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 14:17:29 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

users_1st_nbr = int(input('Enter the first number: '))
users_2nd_nbr = int(input('Enter the second number: '))

result = users_1st_nbr * users_2nd_nbr
print(f'{users_1st_nbr} x {users_2nd_nbr} = {result}')
if result < 0 :
  print('The result is negative')
elif result > 0 :
  print('The result is positive')
else :
  print('The result is positive and negative')