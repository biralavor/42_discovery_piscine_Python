#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameters.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 17:53:45 by umeneses          #+#    #+#              #
#    Updated: 2025/02/26 17:53:46 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == "__main__":
  param_len = len(sys.argv) - 1
  print(f'Number of parameters: {param_len}')