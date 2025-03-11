#!/usr/bin/python3.7

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hello_all.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 11:49:17 by umeneses          #+#    #+#              #
#    Updated: 2025/03/10 11:49:18 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class FirstClass:
  def __init__(self, name):
    self.name = name
  
  def hello(self):
    print(f"Hello {self.name}!")

if __name__ == "__main__":
  greeting_name = "everyone"
  first_instance = FirstClass(greeting_name)
  first_instance.hello()
