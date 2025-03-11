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

def replace_if_empty(saved_notes) :
  for idx in range(0, len(saved_notes)) :
    if saved_notes[idx] == '' :
      saved_notes.remove(saved_notes[idx])
      saved_notes.insert(idx, ' ::  ::')
  return saved_notes

def saved_notes_output(saved_notes) :
  print('\n>>>>>>>>>>>>>>>>>>>>>>>>>')
  print('Here is your saved notes:')
  for idx in range(0, len(saved_notes)) :
    print(f'{idx}. {saved_notes[idx]}')
    idx += 1

def i_got_that() :
  while True :
    if saved_notes[0] == 'STOP' :
      print('No notes saved.')
      exit()
    else :
      users_note = input('I got that! Anything else? : ')
      if users_note == 'STOP' :
        break
    saved_notes.append(users_note)
  return saved_notes

if __name__ == "__main__" :
  saved_notes = []
  users_note = input('What you gotta say? : ')
  saved_notes.append(users_note)
  saved_notes = i_got_that()
  saved_notes = replace_if_empty(saved_notes)
  saved_notes_output(saved_notes)
exit()