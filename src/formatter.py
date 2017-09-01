"""This file contains functions for reading of learning set and formatting."""

import os
import nltk
from text_unidecode import unidecode
from user_param import pos_bool, learning_path

pos_conversion = {
                  'ADJ': 'a',
                  'ADV': 'r',
                  'NOUN': 'n',
                  'VERB': 'v',
                  }
"""dict: Dictionary used to convert POS tag of NLTK to POS tag of Sentiword"""

def formatting(tokens):
  """Convert words tokenized in same format with or without POS tag.

  The format is word.X where X is:
  x (not POS tag)
  a (POS tag: adjective)
  r (POS tag: adverb)
  n (POS tag: noun)
  v (POS tag: verb)

  Parameters
  ----------
  tokens : list
    set of words to format

  Returns
  -------
  list
    Each word of 'tokens' list is formatted.
  """
  tagged = nltk.pos_tag(tokens, 'universal')
  newtagged = []
  for t in tagged:
    if t[1] in pos_conversion:
      newtagged.append(t)
  if not pos_bool:
    newtokens = map(lambda t : t[0] + '.x', newtagged)
  else:
    newtokens = map(lambda (a, b) : (a + '.' + pos_conversion[b]), newtagged)
  return newtokens

def tokenize_string(string):
  """Tokenize and formats a string.

  Parameters
  ----------
  string : str
    The string is the content of a file.

  Returns
  -------
  list
    Each word of 'string' is formatted.
  """
  return formatting(nltk.word_tokenize(unidecode(string)))

def tokenize_file(filename):
  """Tokenize and formats the content of a file.

  Parameters
  ----------
  filename : str
    Path of a file
  Returns
  -------
  list
    Each word of 'filename' is formatted.
  """
  filereader = open(filename, 'r')
  string = filereader.read()
  filereader.close()
  tokens = tokenize_string(string)
  return tokens

