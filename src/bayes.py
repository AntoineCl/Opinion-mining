import numpy as np
import random
from name_class import class_list
from initialisation_class import *
from vocabulary import *


# document: the document to be classified
# estim: the method for estimating probabilities
# return the most likely class according to estim method
def classification(document, estim):
  class_estim = []
  for i in range(nbr_cl):
    class_estim += [estim(class_list[i], document)]
  i = np.argmax(class_estim)
  return class_list[i]

def proba_naive_class(cl):
  return 1./nbr_cl

def proba_weighted_class(cl):
    return float(class_dico[cl]['nbr_occ'])/sum_learning

def add_one(word, cl):
  count = vocabulary[word][cl]
  summ = 0
  for w in vocabulary:
    summ += vocabulary[w][cl]
  return (count + 1) / (voc_size + summ)

def smoothing(word, cl):
  return add_one(word, cl)

def frequency(n):
  return n

def presence(n):
  if n == 0:
    return 0
  else:
    return 1

# doc: a document
# cl: a class
# return PI(P(w|cl)**exp), PI=product
def proba_doc(doc, cl):
  prod = 1
  voc_tmp = {}
  for w in doc:
    if w in vocabulary:
      if w in voc_tmp:
        voc_tmp[w] += 1
      else:
        voc_tmp[w] = 0
    else:
      continue
  for w in voc_tmp:
    exp = frequence(voc_tmp[w])
    # exp = presence(voc_tmp[w])
    prod *= smoothing(w, cl) ** exp
  return prod

# cl: a class
# doc: a document
# return the probability that doc is of class cl by naive bayesian method
def estim_bayes(cl, doc):
  return proba_class(cl)*proba_doc(doc, cl)

def estim_random(cl, doc):
  x = random.random()
  return x




print classification('f', estim_random)
