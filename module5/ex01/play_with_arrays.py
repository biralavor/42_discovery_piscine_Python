#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 15:33:44 by umeneses          #+#    #+#              #
#    Updated: 2025/02/25 15:33:45 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def _array_iterator(original_arr) :
  new_arr = []
  arr_len = len(original_arr)
  for idx in range (arr_len) :
    new_arr.append(original_arr[idx] + 2)
  return new_arr

if __name__ == "__main__" :
  original_arr = [10, 20, 30, 40, 50]
  new_arr = _array_iterator(original_arr)
  print(f'Original array: \t{original_arr}')
  print(f'New array: \t\t{new_arr}')
