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

def remove_duplicates(arr) :
  arr = list(set(arr))
  return arr

def _array_iterator(arr) :
  arr_len = len(arr)
  for idx in range (arr_len) :
    if arr[idx] > 5 :
      arr[idx] = arr[idx] + 2
  return arr

if __name__ == "__main__" :
  new_arr = []
  original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
  new_arr = remove_duplicates(original_arr)
  print(f'Original array: {original_arr}')
  print(f'Removed array: {new_arr}')
  new_arr = _array_iterator(new_arr)
  print(f'Iterated array: {new_arr}')
