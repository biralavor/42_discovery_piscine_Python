#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 12:45:57 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 12:45:58 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

users_nbr = int(input('Please, add a number here: '))
if users_nbr < 0 :
  print('This number is negative.')
elif users_nbr > 0 :
  print('This number is positive.')
else :
  print('This number is both positive and negative.')
