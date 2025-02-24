#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 15:44:14 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 15:44:15 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def table_of_nbr(nbr) :
  table_nbr = []
  idx = 0
  while idx in range(0, 11) :
    table_nbr.append(nbr * idx)
    idx += 1
  return table_nbr

for nbr in range(0, 11) :
  table = table_of_nbr(nbr)
  print(f'Table of {nbr}: {table}')