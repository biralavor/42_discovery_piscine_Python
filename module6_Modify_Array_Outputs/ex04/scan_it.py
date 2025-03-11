#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 17:52:43 by umeneses          #+#    #+#              #
#    Updated: 2025/02/26 17:52:44 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if __name__ == "__main__":
  if len(sys.argv) == 3 :
    tofind = sys.argv[1]
    bigger_txt = sys.argv[2]
    result = re.findall(tofind, bigger_txt)
    total_matches = len(result)
    if result :
      print(total_matches)
    else :
      print('none')
  else :
    print('none')