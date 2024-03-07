#!/usr/bin/env python3

class MyString:
  def __init__(self, value=None):
    if value is None:
      self._value = ""
    elif isinstance (value, str):
      self._value = value
    else:
      print ("The value must be a string.")

  @property
  def value(self):
    return self._value

  @value.setter 
  def value(self, value):
    if isinstance (value, str):
      self._value = value
    else:
      print ("The value must be a string.")

  def is_sentence(self):
    return self._value.endswith('.')

  def is_question(self):
    return self._value.endswith('?')

  def is_exclamation(self):
    return self._value.endswith('!')

  def count_sentences(self):
    sentence_delimiters = ['.', '?', '!']
    num_sentences = 0
    last_char = None

    for char in self._value:
      if char in sentence_delimiters and last_char != char:
        num_sentences += 1
      last_char = char

    return num_sentences

