"""In this file we define the vocabulary used for bayesian classification.
The vocabulary has the following structure:
{word1 : {classe1 : nbr_occ_in_classe1,
          classe2 : ...,
          ...},
 word2 : ...,
 ...}
"""

from user_param import class_name, bool_pos, threshold, max_voc_size
from filereader import formatting
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
    print 'on ajoute'
    dic[key] = intern_dict.copy()
    voc_size += 1

def condition_first_opscore(words, threshold):
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
    id_swn = words[0]
    return id_swn.pos_score() >= threshold or id_swn.neg_score() >= threshold

def condition_mean_opscore(words, threshold):
  if threshold == 0:
    return True
  else:
    pos = 0.
    neg = 0.
    for w in words:
      pos += w.pos_score()
      neg += w.neg_score()
    return pos / len(words) >= threshold or neg / len(words) >= threshold

def condition(words_list):
  """Choice of condition method

  Parameters
  ----------
  word : list

  Returns
  -------
  bool
  """
  return condition_mean_opscore(words_list, threshold)

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
    list_senti_synsets = swn.senti_synsets(nam)
    if list_senti_synsets == []:
      continue
    if condition(list_senti_synsets):
      add_key(voc, nam + '.x')
      i += 1
      # print i
      if i == max_voc_size:
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
    if nam + '.n' in voc or nam + '.a' in voc or nam + '.v' in voc or nam + '.r' in voc:
      continue

    list_n = swn.senti_synsets(nam, 'n')
    if list_n != []:
      if condition(list_n):
        add_key(voc, nam + '.n')
        i += 1
        # print i
        if i == max_voc_size:
          print 'break'
          break

    list_a = swn.senti_synsets(nam, 'a')
    if list_a != []:
      if condition(list_a):
        add_key(voc, nam + '.a')
        i += 1
        # print i
        if i == max_voc_size:
          print 'break'
          break

    list_v = swn.senti_synsets(nam, 'v')
    if list_v != []:
      if condition(list_v):
        add_key(voc, nam + '.v')
        i += 1
        # print i
        if i == max_voc_size:
          print 'break'
          break

    list_r = swn.senti_synsets(nam, 'r')
    if list_r != []:
      if condition(list_r):
        add_key(voc, nam + '.r')
        i += 1
        # print i
        if i == max_voc_size:
          print 'break '
          break

def voc_corpus():
  from learning_class import learning
  learning()
  from learning_class import tokenized_learning_class
  words = []
  for tokens in tokenized_learning_class.values():
    for w in tokens:
      words.append(w)
  freq = nltk.FreqDist(words)
  words_freq = map(lambda (a, b) : a, freq.most_common())

  for i in range(len(words_freq)):
    if bool_pos:
      list_senti_synsets = swn.senti_synsets(words_freq[i][:-2], words_freq[i][-1])
    else:
      list_senti_synsets = swn.senti_synsets(words_freq[i][:-2])
    if list_senti_synsets == []:
      continue
    if condition_mean_opscore(list_senti_synsets, 0.25):
      add_key(voc, words_freq[i])
    if voc_size == max_voc_size:
      break

def select_voc(voc_list):
  n = len(voc_list)
  for i in range(n - 1, -1, -1):
    if voc_size < max_voc_size:
      add_key(voc, voc_list[i][0])
    else:
      break

def voc_sentiword():
  res = {}
  for s_word in swn.all_senti_synsets():
    ll = str(s_word).split('.')
    if len(ll) >= 6:
      continue
    w, pos_tag = ll[0][1:], ll[1]
    if not bool_pos:
      pos_tag = 'x'
    key = w + '.' + pos_tag
    if key not in res:
      res[key] = (s_word.pos_score(), s_word.neg_score())
  sorted_res = sorted(res.items(), key = lambda t : max(t[1][0], t[1][1]))
  select_voc(sorted_res)


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
  if threshold == -1.:
    voc_corpus()
  else:
    voc_sentiword()

def get_voc():
  return voc

def get_voc_size():
  return voc_size

def get_voc_count(word, classname):
  return voc[word][classname]

def set_voc_count(word, classname):
  voc[word][classname] += 1
