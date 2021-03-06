"""This file contains all computation methods for naive bayesian classification."""

import numpy as np
import os
from user_param import class_name, pres_bool, test_path
from initialisation_class import nbr_cl, class_dict, get_sum_learning
from vocabulary import get_voc, get_voc_size, get_voc_count
from formatter import tokenize_string, tokenize_file

voc = {}
"""dict: Vocabulary used for classification"""

voc_size = 0
"""int: Size of vocabulary"""

def proba_naive_class(cl):
  """Return the uniform probability of a class.

  Parameters
  ----------
  cl : string
    A name class

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
    A name class

  Returns
  -------
  float
    The ratio of number of documents in 'cl' class on total number of documents.
  """
  return float(class_dict[cl]['nbr_occ'])/get_sum_learning()

def add_one(word, cl):
  """Apply add-one smoothing to avoid a fraction being zero.

  Parameters
  ----------
  word : str
  cl : str

  Returns
  -------
  float
  """
  return (get_voc_count(word, cl) + 1.) / (voc_size + class_dict[cl]['voc_occ'])

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
  """This function is intended to project an integer in {0, 1}."""
  return 0 if n == 0 else 1

def proba_doc(doc, cl):
  """Return the probability of a document knowing a class.

  See theory for computation method.

  Parameters
  ----------
  doc : list
    A document tokenized into a list
  cl : str
    A class name

  Returns
  -------
  float
    Return product(P(w|cl)**exp)
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
  """Return the probability a document belong to a class.

  See theory for computation method.

  Parameters
  ----------
  doc : list
    A document tokenized into a list
  cl : str
    A class name

  Returns
  -------
  float
    Return the probability of doc multiply by the probability of cl
  """
  a = proba_weighted_class(cl)
  b = proba_doc(doc, cl)
  return a * b

def doc_classification(doc):
  """Return the most likely class of a document.

  Parameters
  ----------
  doc : list
    A document tokenized into a list

  Returns
  -------
  str
    The name of the most likely class
  """
  class_estim = []
  for i in range(nbr_cl):
    class_estim += [estim_bayes(doc, class_name[i])]
  i = np.argmax(class_estim)
  return class_name[i]

def classification():
  """Return all the documents of test set with their estimated classification.

  Parameters
  ----------

  Returns
  -------
  dict
    The keys are paths of test set and values are their estimated
    classification.
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
  return classified




