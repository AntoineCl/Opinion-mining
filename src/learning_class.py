import os
import nltk
from vocabulary import vocabulary
from filereader import tokenize_file
from initialisation_class import class_dico
from learning_path import learning_path_list
from name_class import class_list




def handle_token(tokens, classname):
  for t in tokens:
    if t in vocabulary:
      vocabulary[t][classname] += 1 # on met a jour les occurence de vocabulaire


# input: directory: absolute path
def learning_dir(directory, classname, bool_pos): # tous les fichiers d'un repertoire
  list_file = os.listdir(directory)
  list_tokens = []
  class_dico[classname]['nbr_occ'] += len(list_file)
  # print list_file
  for f in list_file:
    # print f
    # print directory + f
    tokens = tokenize_file(directory + f, bool_pos)
    handle_token(tokens, classname)
    list_tokens += tokens
    # print tokens
    # print list_tokens


# input: filename: absolute path
def learning_file(filename, classname, bool_pos): # toutes les lignes d'un fichier
  tokens = tokenize_file(filename, bool_pos)
  handle_token(tokens, classname)

  filereader = open(filename, 'r')
  line = filereader.readline()

  i = 1
  while line != '':
    line = filereader.readline()
    i += 1
    print i

  filereader.close()
  class_dico[classname]['nbr_occ'] += len(i)


def learning(bool_pos):
  print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa_learning'
  print vocabulary
  n = len(learning_path_list)
  for i in range(n):
    if os.path.isdir(learning_path_list[i]):
      learning_dir(learning_path_list[i], class_list[i], bool_pos)
    else:
      learning_file(learning_path_list[i], class_list[i], bool_pos)
  print vocabulary



# learning_dir('/home/antoine/documents/tmp/')
# learning_file('/home/antoine/documents/tmp/tmp1.txt', 'positive', False)

# learning(False)



