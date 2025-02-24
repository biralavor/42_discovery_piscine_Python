#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 12:49:12 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 12:49:13 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

password = 'Python is awesome'
access_granted = 'Access granted'
access_denied = 'Access denied'
users_password = str(input('Enter the password: '))

if users_password == password :
  print(access_granted)
else :
  print(access_denied)
