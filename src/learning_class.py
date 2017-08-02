import os
import nltk
from vocabulary import voc_count_one
from filereader import tokenize_file
from initialisation_class import add_count
from learning_set import learning_path
from name_class import class_list




def handle_token(voc, tokens, classname):
  for t in tokens:
    if t in voc:
      voc_count_one(voc, t, classname)


def learning_dir(voc, bool_pos, directory, classname): # tous les fichiers d'un repertoire
  file_list = os.listdir(directory)
  tokens_list = []
  add_count(classname, len(file_list))
  # print file_list
  for f in file_list:
    # print f
    # print directory + f
    tokens = tokenize_file(bool_pos, directory + f)
    handle_token(voc, tokens, classname)
    tokens_list += tokens
    # print tokens
    # print tokens_list


def learning_file(voc, bool_pos, filename, classname): # toutes les lignes d'un fichier
  tokens = tokenize_file(bool_pos, filename)
  handle_token(voc, tokens, classname)

  filereader = open(filename, 'r')
  line = filereader.readline()
# 'modifier cette partie en utilisant tokenize_string'
  i = 1
  while line != '':
    line = filereader.readline()
    i += 1
    # print i

  filereader.close()
  add_count(classname, i)


def learning(voc, bool_pos):
  print len(voc)
  print voc
  n = len(learning_path)
  for i in range(n):
    if os.path.isdir(learning_path[i]):
      learning_dir(voc, bool_pos, learning_path[i], class_list[i])
    else:
      learning_file(voc, bool_pos, learning_path[i], class_list[i])
  print voc




