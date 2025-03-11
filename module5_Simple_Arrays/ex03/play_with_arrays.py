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

def set_iterator(cleaned_set) :
  cleaned_list = list(cleaned_set)
  for value in cleaned_list.copy() :
    if value > 5 :
      cleaned_list[cleaned_list.index(value)] += 2
    else :
      cleaned_list.remove(value)
  print(f'Inside set_iterator: \t{cleaned_list}')
  return set(cleaned_list)

if __name__ == "__main__" :
  original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
  arr_to_set = set(original_arr)
  iterated_set = {}
  print(f'Original array: \t{original_arr}')
  print(f'Array to Set: \t\t{arr_to_set}')
  iterated_set = set_iterator(arr_to_set)
  print(f'Iterated set: \t\t{iterated_set}')
