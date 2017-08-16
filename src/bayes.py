"""This file contains all computation methods for naive bayesian classification"""

import numpy as np
import os
from user_param import class_name, pres_bool, test_path
from initialisation_class import nbr_cl, class_dict, get_sum_learning
from vocabulary import get_voc, get_voc_size, get_voc_count
from filereader import tokenize_string, tokenize_file

voc = {}
"""dict: vocabulary used for classification"""

voc_size = 0
"""int: size of vocabulary"""

def proba_naive_class(cl):
  """Return the uniform probability of a class.

  Parameters
  ----------
  cl : string
    a name class

  Returns
  -------
  float
  """
  return 1./nbr_cl

def proba_weighted_class(cl):
  """Return the weighted probability of a class.

  Parameters
  ----------
  cl : str
    a name class

  Returns
  -------
  float
    The ratio of number of document in 'cl' class on total number of document
  """
  return float(class_dict[cl]['nbr_occ'])/get_sum_learning()

def add_one(word, cl):
  """Apply add-one smoothing (see theory).

  Parameters
  ----------
  word : str
  cl : str

  Returns
  -------
  float
  """
  count = get_voc_count(word, cl)
  # summ = 0
  # for w in voc:
    # summ += voc[w][cl]
  # return (count + 1.) / (voc_size + summ)
  return (count + 1.) / (voc_size + class_dict[cl]['voc_occ'])

def smoothing(word, cl):
  """Apply the selected smoothing.

  Parameters
  ----------
  word : str
  cl : str

  Returns
  -------
  float
  """
  return add_one(word, cl)

def frequency(n):
  return n

def presence(n):
  """This function is intended to project an integer in {0, 1}.
  See theory for utility.
  """
  if n == 0:
    return 0
  else:
    return 1

def proba_doc(doc, cl):
  """Return the probability a document knowing a class under assumptions of the
  theory.
  See theory for computation method.

  Parameters
  ----------
  doc : list
    a document tokenized into a list
  cl : str
    a class name

  Returns
  -------
  float
    return product(P(w|cl)**exp)
  """
  prod = 1
  voc_tmp = {}
  method = presence if pres_bool else frequency
  for w in doc:
    if w in voc:
      if w in voc_tmp:
        voc_tmp[w] += 1
      else:
        voc_tmp[w] = 1
    else:
      continue
  for w in voc_tmp:
    exp = method(voc_tmp[w])
    prod *= smoothing(w, cl) ** exp
  return prod

def estim_bayes(doc, cl):
  """Return the probability a document belong to a class under assumptions of
  the theory.
  See theory for computation method.

  Parameters
  ----------
  doc : list
    a document tokenized into a list
  cl : str
    a class name

  Returns
  -------
  float
    Return the probability of doc multiply by the probability of cl
  """
  a = proba_weighted_class(cl)
  b = proba_doc(doc, cl)
  print str(a) + ' * ' + str(b)
  return a * b
  # return proba_weighted_class(cl)*proba_doc(doc, cl)

def doc_classification(doc):
  """Return the most likely class of a document.

  Parameters
  ----------
  doc : list
    a document tokenized into a list

  Returns
  -------
  str
    the name of the most likely class
  """
  class_estim = []
  for i in range(nbr_cl):
    class_estim += [estim_bayes(doc, class_name[i])]
  i = np.argmax(class_estim)
  print ''
  print ''
  return class_name[i]

def classification():
  """Return all the documents of test set with their estimated classification.

  Parameters
  ----------

  Returns
  -------
  dict
    The keys are paths of test set and values are their estimated classification.
  """
  global voc
  global voc_size
  voc = get_voc()
  voc_size = get_voc_size()
  classified = {}
  n = len(test_path)
  tokens = []
  for i in range(n):
    if os.path.isdir(test_path[i]):
      file_list = os.listdir(test_path[i])
      m = len(file_list)
      for j in range(m):
        tokens = tokenize_file(test_path[i] + file_list[j])
        classified[test_path[i] + file_list[j]] = doc_classification(tokens)
    else:
        filereader = open(test_path[i], 'r')
        line = filereader.readline()
        j = 1
        while line != '':
          tokens = tokenize_string(line)
          classified[test_path[i] + '_line_' + str(j)] = doc_classification(tokens)
          line = filereader.readline()
          j += 1
        filereader.close()
    print 'classified : ' + test_path[i]
  return classified




