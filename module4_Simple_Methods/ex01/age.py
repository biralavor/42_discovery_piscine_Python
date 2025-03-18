#!/usr/bin/python3.12

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    age.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 17:27:31 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 17:27:32 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class milestoneCalculator:
  def __init__(self, age, milestone):
    self.age = age
    self.milestone = milestone

  def input_validation(self):
    while True:
      nbr = input('Please, tell me your age: ')
      try:
        users_age = int(nbr)
        break
      except ValueError:
        if nbr == "":
          sys.stderr.write("You didn't enter anything. T.T!\n")
        else:
          sys.stderr.write(f"'{nbr}' wasn't a number. Try again!\n")
    return users_age
  
  def calculator_runner(self, users_age, milestone):
    if users_age < 0:
      sys.stderr.write("It seems you're NOT born yet. O.o\n")
      users_age = self.input_validation()
    for loop in range(1, 4):
      next_age = users_age + (milestone * loop)
      next_mile = milestone * loop
      print(f'In {next_mile} years, you will be {next_age} years old.')

if __name__ == "__main__":
  milestone = 10
  arg_input = milestoneCalculator(0, 0)
  users_age = arg_input.input_validation()
  arg_input.calculator_runner(users_age, milestone)