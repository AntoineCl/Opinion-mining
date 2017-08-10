"""This file contains function for reading of learning set and formatting.
"""

import os
import nltk
from user_param import bool_pos

pos_conversion = {
                  'ADJ': 'a',
                  # 'ADP': ,
                  'ADV': 'r',
                  # 'CONJ': ,
                  # 'DET': ,
                  'NOUN': 'n',
                  # 'NUM': ,
                  # 'PRT': ,
                  # 'PRON': ,
                  'VERB': 'v',
                  # '.': ,
                  # 'X': ,
                  }
"""dict: is used to convert POS tag of NLTK to POS tag of Sentiword
"""

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
  # print tokens
  if not bool_pos:
    newtokens = list(map(lambda t : t + '.x', tokens))
  else:
    newtokens = []
    tagged = nltk.pos_tag(tokens, 'universal')
    # newtokens = list(map(lambda (a, b) : (a, pos_conversion[b]), tagged)) # existence of b?
    n = len(tagged)
    for i in range(n):
      if tagged[i][1] in pos_conversion:
        newtokens += [tagged[i][0] + '.' + pos_conversion[tagged[i][1]]]
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
  tokens = nltk.word_tokenize(string)
  # print tokens
  newtokens = formatting(tokens)
  # print newtokens
  return newtokens

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
  print 'tokenize : ' + filename
  filereader = open(filename, 'r')
  string = filereader.read()
  filereader.close()
  tokens = tokenize_string(string)
  return tokens



