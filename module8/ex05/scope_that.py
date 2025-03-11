#!/usr/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 12:30:17 by umeneses          #+#    #+#              #
#    Updated: 2025/03/11 12:30:18 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class scope_that:
  def __init__(self):
    pass

  def input_validation(self, user_input):
    try:
      nbr = (int(user_input))
    except ValueError:
      raise ValueError("Please enter a number")
    return nbr

  def add_one(self, nbr):
    return nbr + 1
  
  def scope_init(self, user_input):
    validated_input = scope.input_validation(user_input)
    result = scope.add_one(validated_input)
    return result

if __name__ == "__main__":
  user_input = 42
  scope = scope_that()
  result = scope.scope_init(user_input)
  print(f"Here was value at main >>> {user_input}")
  print(f"Here is the result >>>>>>> {result}")
