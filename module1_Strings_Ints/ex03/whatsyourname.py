#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatsyourname.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 12:29:13 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 12:29:14 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

users_first_name = input('Hey, what\'s your first name? : ')
users_last_name = input('Hey, what\'s your last name? : ').strip()
greeting = 'Well, pleased to meet you,'

print(f'{greeting} {users_first_name.strip()} {users_last_name}.')