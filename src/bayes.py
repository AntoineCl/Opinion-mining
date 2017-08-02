import numpy as np
import random
import os
from name_class import class_list
from initialisation_class import nbr_cl, class_dico, get_sum_learning
from vocabulary import get_voc_count
from test_set import test_path
from filereader import tokenize_string, tokenize_file

voc = {}
voc_size = 0


def proba_naive_class(cl):
  return 1./nbr_cl

def proba_weighted_class(cl):
  return float(class_dico[cl]['nbr_occ'])/get_sum_learning()

def add_one(voc, word, cl):
  count = get_voc_count(voc, word, cl)
  summ = 0
  for w in voc:
    summ += voc[w][cl]
  # print 'add_one :'
  # print '  count : ' + str(count)
  # print '  voc_size : ' + str(voc_size)
  # print '  summ : ' + str(summ)
  # print '    ' + str((count + 1) / (voc_size + summ))
  return (count + 1.) / (voc_size + summ)

def smoothing(voc, word, cl):
  return add_one(voc, word, cl)

def frequency(n):
  return n

def presence(n):
  if n == 0:
    return 0
  else:
    return 1

# doc: a document
# cl: a class
# return product(P(w|cl)**exp)
def proba_doc(voc, pres_bool, doc, cl):
  prod = 1
  voc_tmp = {}
  for w in doc:
    if w in voc:
      if w in voc_tmp:
        voc_tmp[w] += 1
      else:
        voc_tmp[w] = 1
    else:
      continue
  for w in voc_tmp:
    # exp = frequency(voc_tmp[w])
    exp = presence(voc_tmp[w])
    exp = presence(voc_tmp[w]) if pres_bool else frequency(voc_tmp[w])
    prod *= smoothing(voc, w, cl) ** exp
  return prod

# cl: a class
# doc: a document
# return the probability that doc is of class cl by naive bayesian method
def estim_bayes(voc, pres_bool, doc, cl):
  a = proba_weighted_class(cl)
  b = proba_doc(voc, pres_bool, doc, cl)
  print str(a) + ' * ' + str(b)
  return a * b
  # return proba_weighted_class(cl)*proba_doc(doc, cl)

def estim_random(doc, cl):
  x = random.random()
  return x

# document: the document to be classified
# return the most likely class according to estim method
def doc_classification(voc, pres_bool, document):
  class_estim = []
  for i in range(nbr_cl):
    class_estim += [estim_bayes(voc, pres_bool, document, class_list[i])]
  i = np.argmax(class_estim)
  print class_estim
  return class_list[i]


def classification(voc, bool_pos, pres_bool):
  classified = {}
  n = len(test_path)
  tokens = []
  for i in range(n):
    if os.path.isdir(test_path[i]):
      file_list = os.listdir(test_path[i])
      m = len(file_list)
      for j in range(m):
        tokens = tokenize_file(bool_pos, test_path[i] + file_list[j])
        classified[test_path[i] + file_list[j]] = doc_classification(voc, pres_bool, tokens)
    else:
        filereader = open(test_path[i], 'r')
        line = filereader.readline()
        j = 1
        while line != '':
          tokens = tokenize_string(bool_pos, line)
          classified[test_path[i] + ' line ' + str(j)] = doc_classification(voc, pres_bool, tokens)
          line = filereader.readline()
          j += 1
        filereader.close()
    print 'classified : ' + test_path[i]
  return classified




