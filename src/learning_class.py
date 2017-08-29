"""This file contains main function for learning phase."""

import os
import nltk
from vocabulary import voc, get_voc
from filereader import tokenize_string, tokenize_file
from initialisation_class import class_dict, add_count
from user_param import class_name, corpus_bool, threshold, learning_path


first_learnset_reading = True
"""bool: True iff learning set has'nt been read"""

tokenized_learning_class = {}
"""dict: Contains learning set tokenized if it has already been read"""


def init_tokenized_learning_class():
  """Initialize 'tokenized_learning_class' with name class as key and empty
  list as value.
  """
  for cl in class_name:
    tokenized_learning_class[cl] = []

def handle_token(tokens, classname):
  """This function counts occurrence of vocabulary words (formatted) appearing
  in documents of 'classname' class.

  Parameters
  ----------
  tokens : list
    A document of 'classname' class tokenized into a list
  classname : str

  Returns
  -------
  None
  """
  i = 0
  for t in tokens:
    if t in voc:
      i += 1
      voc[t][classname] += 1
      class_dict[classname]['voc_occ'] += 1

def handle_tokenized_learning():
  """Apply 'handle_token' function to learning set tokenized."""
  for k, v in tokenized_learning_class.items():
    handle_token(v, k)

def learning_dir(directory, classname):
  """Read all files of a directory for learning.

  We condider the directory is a learning set for class 'classname'. Files are
  tokenized.

  Parameters
  ----------
  directory : str
    Relative path of directory containing files
  classname : str

  Returns
  -------
  None
    The learning set of class 'classname' is learned.
  """
  file_list = os.listdir(directory)
  tokens_list = []
  add_count(classname, len(file_list))
  for f in file_list:
    tokens = tokenize_file(directory + f)
    tokens_list += tokens
  tokenized_learning_class[classname] += tokens_list

def learning_file(filename, classname):
  """Read all lines of a file for learning.

  We condider the file is a learning set for class 'classname'. Lines are
  tokenized.

  Parameters
  ----------
  filename : str
    Relative path of file
  classname : str

  Returns
  -------
  None
    The learning set of class 'classname' is learned.
  """
  filereader = open(filename, 'r')
  line = filereader.readline()
  string = line
  i = 1
  while line != '':
    line = filereader.readline()
    string += line
    i += 1
  filereader.close()
  tokens = tokenize_string(string)
  add_count(classname, i)
  tokenized_learning_class[classname] = tokens

def main_learning():
  """Main function for learning.

  It detects if learning sets are directories filled with files or files filled
  with lines and tokenize them.
  """
  n = len(learning_path)
  for i in range(n):
    if os.path.isdir(learning_path[i]):
      learning_dir(learning_path[i], class_name[i])
    else:
      learning_file(learning_path[i], class_name[i])

def learning():
  """Apply 'main_learning' function and/or apply 'handle_tokenized_learning'
  function.

  If 'corpus_bool' is activated, 'learning' is executed twice: one time for
  define the vocabulary and one time to handle tokens created the first time.
  If 'corpus_bool' is not activated, 'learning' is executed once and so
  tokenizing and handling are executed sequentially.
  """
  global first_learnset_reading
  if corpus_bool:
    if first_learnset_reading:
      init_tokenized_learning_class()
      main_learning()
      first_learnset_reading = False
    else:
      handle_tokenized_learning()
  else:
    init_tokenized_learning_class()
    main_learning()
    handle_tokenized_learning()
    first_learnset_reading = False



