#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 17:45:33 by umeneses          #+#    #+#              #
#    Updated: 2025/02/26 17:45:34 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == "__main__":
  if len(sys.argv) > 2 :
    param_len = len(sys.argv)
    for idx in range (1, param_len) :
      print(sys.argv[param_len - idx])
  else :
    print('none')