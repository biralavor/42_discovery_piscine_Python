#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 15:44:18 by umeneses          #+#    #+#              #
#    Updated: 2025/02/25 15:44:19 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

MAX = 5

def _array_iterator(original_arr) :
  new_arr = []
  arr_len = len(original_arr)
  for idx in range (arr_len) :
    if original_arr[idx] > MAX :
      new_arr.append(original_arr[idx] + 2)
  return new_arr

if __name__ == "__main__" :
  original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
  new_arr = _array_iterator(original_arr)
  print(f'Original array: {original_arr}')
  print(f'New array: {new_arr}')
