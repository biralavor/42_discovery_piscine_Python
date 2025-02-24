#!/usr/bin/python3.8

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    i_got_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: umeneses <umeneses@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 15:27:29 by umeneses          #+#    #+#              #
#    Updated: 2025/02/24 15:27:30 by umeneses         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

saved_notes = []
users_note = input('What you gotta say? : ')
saved_notes.append(users_note)
while True :
  users_note = input('I got that! Anything else? : ')
  if users_note == 'STOP' :
    break
  saved_notes.append(users_note)
if len(saved_notes) == 0 :
  print('No notes saved.')
else :
  print('\n>>>>>>>>>>>>>>>>>>>>>>>>>')
  print('Here is your saved notes:')
  for idx in range(0, len(saved_notes)) :
    print(f'{idx}. {saved_notes[idx]}')
    idx += 1
exit()