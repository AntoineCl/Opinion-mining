"""In this file we define the vocabulary used for bayesian classification.
The vocabulary has the following structure:
{word1 : {classe1 : nbr_occ_in_classe1,
          classe2 : ...,
          ...},
 word2 : ...,
 ...}
"""

from user_param import class_name, bool_pos, threshold, voc_size_a_priori
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

wn_list = wn.all_synsets()
"""generator: allows iteration on objects of wordnet"""

swn_list = swn.all_senti_synsets()
"""generator: allows iteration on objects of sentiwordnet"""

voc = {}
"""dict: vocabulary used for classification"""

voc_size = 0

intern_dict = {}
"""dict: necessary for construction of voc"""

def init_intern_dict():
  """Initialize inter_dict.
  Keys are name of class and values are 0
  """
  for name in class_name:
    intern_dict[name] = 0

def add_key(dic, key):
  """Add a key in a dictionary.

  Parameters
  ----------
  dic : dict
  key : str

  Returns
  -------
  None
    The value of the added key is a copy of inter_dict
  """
  global voc_size
  if key not in dic:
    dic[key] = intern_dict.copy()
    voc_size += 1

# def voc_count_one(word, classname):
  # voc[word][classname] += 1

def condition_opscore(word, threshold):
  """Condition on value of opinion score of a word in Sentiword.

  Parameters
  ----------
  word : str
  threshold : float
    the threshold of opinion score

  Returns
  -------
  bool
  """
  if threshold == 0:
    return True
  else:
    return word.pos_score() >= threshold or word.neg_score() >= threshold

def condition(word):
  """Choice of condition method

  Parameters
  ----------
  word : str

  Returns
  -------
  bool
  """
  return condition_opscore(word, threshold)

def voc_basis_sentiword(words):
  """Define the vocabulary without using part-of-speech tagging

  Parameters
  ----------

  Returns
  -------
  None
    The vocabulary contain words respecting the condition
  """
  i = 0
  # for w in wn_list:
    # tmp = str(w.name()).split('.')
    # if len(tmp) >= 4:
      # continue
    # nam = tmp[0] # nam = le nom comme il est dans le texte
  for nam in words:
    if nam + '.x' in voc:
      continue
    list_senti_synsets = list(swn.senti_synsets(nam))
    if list_senti_synsets == []:
      continue
    id_swn = list_senti_synsets[0] # id_swn = la ref sentiword
    if condition(id_swn):
      add_key(voc, nam + '.x')
      i += 1
      # print i
      if i == voc_size_a_priori:
        print 'break'
        break

def voc_pos_sentiword(words):
  """Define the vocabulary using part-of-speech tagging

  Parameters
  ----------

  Returns
  -------
  None
    The vocabulary contain words respecting the condition
  """
  i = 0
  # for w in wn_list:
    # tmp = str(w.name()).split('.')
    # if len(tmp) >= 4:
      # continue # on ignore les cas particulier ou le nom contient un '.' par facilite
    # nam = tmp[0] # nam = le nom comme il est dans le texte
  for nam in words:
    if nam+'.n' in voc or nam+'.a' in voc or nam+'.v' in voc or nam+'.r' in voc:
      continue

    list_n = list(swn.senti_synsets(nam, 'n'))
    if list_n != []:
      id_swn_n = list_n[0]
      if condition(id_swn_n):
        add_key(voc, nam + '.n')
        i += 1
        # print i
        if i == voc_size_a_priori:
          print 'break with'
          break

    list_a = list(swn.senti_synsets(nam, 'a'))
    if list_a != []:
      id_swn_a = list_a[0]
      if condition(id_swn_a):
        add_key(voc, nam + '.a')
        i += 1
        # print i
        if i == voc_size_a_priori:
          print 'break'
          break

    list_v = list(swn.senti_synsets(nam, 'v'))
    if list_v != []:
      id_swn_v = list_v[0]
      if condition(id_swn_v):
        add_key(voc, nam + '.v')
        i += 1
        # print i
        if i == voc_size_a_priori:
          print 'break'
          break

    list_r = list(swn.senti_synsets(nam, 'r'))
    if list_r != []:
      id_swn_r = list_r[0]
      if condition(id_swn_r):
        add_key(voc, nam + '.r')
        i += 1
        # print i
        if i == voc_size_a_priori:
          print 'break '
          break

def word_nltk_movie_corpus():
  from nltk.corpus import movie_reviews
  words = []
  for w in movie_reviews.words():
    # print w
    words.append(w)
  words_freq = nltk.FreqDist(words)
  # return list(words_freq.keys())[:voc_size_a_priori]
  return list(words_freq.keys())

def word_wn():
  words = []
  for w in wn_list:
    tmp = str(w.name()).split('.')
    if len(tmp) >= 4:
      continue
    nam = tmp[0] # nam = le nom comme il est dans le texte
    words.append(nam)
  return words


def define_voc():
  """Main function for define vocabulary by selecting the appropriated method
  (with or without POS tagging)

  Parameters
  ----------

  Returns
  -------
  None
    The vocabulary is constructed
  """
  init_intern_dict()
  if bool_pos:
    voc_pos_sentiword(word_wn())
  else:
    voc_basis_sentiword(word_nltk_movie_corpus())
  print voc_size

def get_voc():
  return voc

def get_voc_size():
  return voc_size

def get_voc_count(word, classname):
  return voc[word][classname]


