#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 16:59:47 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 16:59:48 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
  while True :
    users_input = input('Give me a word: ')
    if users_input.isalpha() :
      break
    else :
      print('Only letters are allowed.')
  users_input = users_input.upper()
  print(users_input)