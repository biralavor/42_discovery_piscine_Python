#!/usr/bin/python3.12

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

class iGotThat:
  def __init__(self, saved_notes):
    self.saved_notes = saved_notes

  def replace_if_empty(self, saved_notes):
    for idx in range(0, len(self.saved_notes)):
      if self.saved_notes[idx] == '' :
        self.saved_notes.remove(self.saved_notes[idx])
        self.saved_notes.insert(idx, ': : : : : :')
    return self.saved_notes

  def input_catcher(self):
    user_input = input('What you gotta say? : ')
    return user_input

  def saved_notes_output(self, saved_notes):
    notes_msg = 'Here is your saved notes:'
    notes_msg_len = len(notes_msg)
    for _ in range(0, notes_msg_len):
      print('>', end="")
    print("\n" + notes_msg)
    for idx in range(len(saved_notes)):
      print(f'{idx}. {saved_notes[idx]}')
      idx += 1
    for _ in range(notes_msg_len):
      print('>', end="")
    print('')

  def save_my_notes(self) :
    while True:
      if self.saved_notes[0] == 'STOP':
        print('No notes saved.')
        exit()
      else:
        users_note = input('I got that! Anything else? Say "STOP" to end it : ')
        if users_note == 'STOP':
          break
      self.saved_notes.append(users_note)
    return self.saved_notes

if __name__ == "__main__":
  saved_notes = []
  digital_post_it = iGotThat(saved_notes)
  saved_notes.append(digital_post_it.input_catcher())
  saved_notes = digital_post_it.save_my_notes()
  saved_notes = digital_post_it.replace_if_empty(saved_notes)
  digital_post_it.saved_notes_output(saved_notes)