#!/usr/bin/python3.8

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

def milestone_calculator(users_age, milestone) :
  if users_age < 0 :
    print("You are not born yet.")
    users_age = input_validation()
  for loop in range(1, 4):
    next_age = users_age + (milestone * loop)
    next_mile = milestone * loop
    print(f'In {next_mile} years you will be {next_age} years old.')

def input_validation() :
  while True :
    users_age = input('Please tell me your age: ')
    try :
      users_age = int(users_age)
      break
    except ValueError :
      print("Your input wasn't a number. Please, try again!")
  return users_age

if __name__ == "__main__" :
  users_age = input_validation()
  milestone = 10
  milestone_calculator(users_age, milestone)