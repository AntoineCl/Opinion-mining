"""This file contains function for reading of learning set and formatting."""

import os
import nltk
from user_param import bool_pos, learning_path

pos_conversion = {
                  'ADJ': 'a',
                  'ADV': 'r',
                  'NOUN': 'n',
                  'VERB': 'v',
                  }
"""dict: is used to convert POS tag of NLTK to POS tag of Sentiword"""

def formatting(tokens):
  """Need that words are in same format with or without POS tag. The format is
  word.X where X is:
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
    Each word of 'tokens' list is formatting
  """
  tagged = nltk.pos_tag(tokens, 'universal')
  newtagged = []
  for t in tagged:
    if t[1] in pos_conversion:
      newtagged.append(t)
  if not bool_pos:
    newtokens = map(lambda t : t[0] + '.x', newtagged)
  else:
    newtokens = map(lambda (a, b) : (a + '.' + pos_conversion[b]), newtagged) # existence of b? -> ok because the sort is made firstly
  return newtokens

def tokenize_string(string):
  """Tokenize and formats a string (the string is the content of a file).

  Parameters
  ----------
  string : str

  Returns
  -------
  list
    Each word of 'string' is formatting
  """
  return formatting(nltk.word_tokenize(string))

def tokenize_file(filename):
  """Tokenize and formats the content of a file.

  Parameters
  ----------
  filename : str
    Relative path
  Returns
  -------
  list
    Each word of 'filename' is formatting
  """
  filereader = open(filename, 'r')
  string = filereader.read()
  filereader.close()
  tokens = tokenize_string(string)
  return tokens


# def tokenize_dir(dirname):
  # file_list = os.listdir(dirname)
  # tokens = []
  # for f in file_list:
    # tokens += tokenize_file(directory + f)
  # return tokens



# def tokenize_set():
  # n = len(learning_path)
  # tokens = []
  # for i in range(n):
    # if os.path.isdir(path):
      # tokens += tokenize_dir(path, class_name[i])
    # else:
      # tokens += tokenize_file(path, class_name[i])
  # return tokens


