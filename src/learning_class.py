#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""This file contains main function for learning phase."""

import os
import nltk
from vocabulary import voc, get_voc
from filereader import tokenize_file
from initialisation_class import class_dict, add_count
from user_param import class_name, learning_path


# corpus_words = {}
# """dict: words not present in vocabulary but appearing in learning corpus"""


def handle_token(tokens, classname):
  """This function counts occurence of vocabulary words (formatted) appearing in
  documents of 'classname' class.

  Parameters
  ----------
  tokens : list
    A document of 'classname' class tokenized into a list
  classname : str

  Returns
  -------
  None
  """
  print tokens
  for t in tokens:
    if t in voc:
      # voc_count_one(t, classname)
      voc[t][classname] += 1
      print class_dict
      class_dict[classname]['voc_occ'] += 1
    # else:
      # if t in corpus_words:
        # if classname in corpus_words[t]:
          # corpus_words[t][classname] += 1
        # else:
          # corpus_words[t][classname] = 1
      # else:
        # corpus_words[t] = {classname : 1}


def learning_dir(directory, classname):
  """Read all files of a directory for learning. We condider the directory is a
  learning set for class 'classname'. Files are tokenized and we apply
  'handle_token' function.

  Parameters
  ----------
  directory : str
    Relative path of directory containing files
  classname : str

  Returns
  -------
  None
    The learning set of class 'classname' is learned
  """
  file_list = os.listdir(directory)
  # tokens_list = []
  add_count(classname, len(file_list))
  for f in file_list:
    tokens = tokenize_file(directory + f)
    handle_token(tokens, classname)
    # tokens_list += tokens


def learning_file(filename, classname):
  """Read all lines of a file for learning. We condider the file is a learning
  set for class 'classname'. Lines are tokenized and we apply  'handle_token'
  function.

  Parameters
  ----------
  filename : str
    Relative path of file
  classname : str

  Returns
  -------
  None
    The learning set of class 'classname' is learned
  """
  tokens = tokenize_file(filename)
  handle_token(tokens, classname)

  filereader = open(filename, 'r')
  line = filereader.readline()
# modifier cette partie en utilisant tokenize_string
  i = 1
  while line != '':
    line = filereader.readline()
    i += 1
    # print i

  filereader.close()
  add_count(classname, i)


def learning():
  """Main function for learning. Detect if learning sets are directories filled
  with files or files filled with lines.

  Parameters
  ----------

  Returns
  -------
  None
    All learning sets have been handled
  """
  # print get_voc()
  n = len(learning_path)
  for i in range(n):
    if os.path.isdir(learning_path[i]):
      learning_dir(learning_path[i], class_name[i])
    else:
      learning_file(learning_path[i], class_name[i])
  # print get_voc()



