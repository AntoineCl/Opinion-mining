"""In this file we define the vocabulary used for bayesian classification.
The vocabulary has the following structure:
{word1 : {classe1 : nbr_occ_in_classe1,
          classe2 : ...,
          ...},
 word2 : ...,
 ...}
"""

from user_param import class_name, pos_bool, corpus_bool, threshold, max_voc_size
from filereader import formatting
import nltk
from nltk.corpus import sentiwordnet as swn


voc = {}
"""dict: vocabulary used for classification"""

voc_size = 0
"""int: size of vocabulary"""

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

def condition_first_opscore(words, threshold):
  """Condition on value of opinion score of a word in Sentiword.
  The used opinion score is that of first word in the synonymous list.

  Parameters
  ----------
  words : list
    list of synonymous
  threshold : float
    the threshold of opinion score

  Returns
  -------
  bool
    Return True iff the opinion score is greater than threshold
  """
  if threshold == 0:
    return True
  else:
    id_swn = words[0]
    return id_swn.pos_score() >= threshold or id_swn.neg_score() >= threshold

def condition_average_opscore(words, threshold):
  """Condition on value of opinion score of a word in Sentiword.
  The used opinion score is the average of opinion scores of word in the
  synonymous list.

  Parameters
  ----------
  words : list
    list of synonymous
  threshold : float
    the threshold of opinion score

  Returns
  -------
  bool
    Return True iff the opinion score is greater than threshold
  """
  if threshold == 0:
    return True
  else:
    pos = 0.
    neg = 0.
    for w in words:
      pos += w.pos_score()
      neg += w.neg_score()
    return pos / len(words) >= threshold or neg / len(words) >= threshold

def condition(words):
  """Choice of condition method.

  Parameters
  ----------
  words : list

  Returns
  -------
  bool
  """
  return condition_average_opscore(words, threshold)

def voc_corpus():
  """Construct the vocabulary based on most frequent opinion words in learning
  set.

  Parameters
  ----------

  Returns
  -------
  None
    The vocabulary is constructed
  """
  from learning_class import learning
  learning()
  from learning_class import tokenized_learning_class
  words = []
  for tokens in tokenized_learning_class.values():
    # for w in tokens:
      # words.append(w)
    words += tokens
  freq = nltk.FreqDist(words)
  words_freq = map(lambda (a, b) : a, freq.most_common())

  for i in range(len(words_freq)):
    if pos_bool:
      list_senti_synsets = swn.senti_synsets(words_freq[i][:-2], words_freq[i][-1])
    else:
      list_senti_synsets = swn.senti_synsets(words_freq[i][:-2])
    if list_senti_synsets == []:
      continue
    if condition(list_senti_synsets):
      add_key(voc, words_freq[i])
    if voc_size == max_voc_size:
      break

def select_voc(voc_list):
  """Add the 'max_voc_size' first words of voc_list in the vocabulary.

  Parameters
  ----------
  voc_list : list

  Returns
  -------
  None
  """
  n = len(voc_list)
  for i in range(n - 1, -1, -1):
    if voc_size < max_voc_size:
      add_key(voc, voc_list[i][0])
    else:
      break

def voc_sentiword():
  """Construct the vocabulary based on words with the biggest opinion score in
  Sentiword.

  Parameters
  ----------

  Returns
  -------
  None
    The vocabulary is constructed
  """
  res = {}
  for s_word in swn.all_senti_synsets():
    ll = str(s_word).split('.')
    if len(ll) >= 6:
      continue
    w, pos_tag = ll[0][1:], ll[1]
    if not pos_bool:
      pos_tag = 'x'
    key = w + '.' + pos_tag
    if key not in res:
      res[key] = (s_word.pos_score(), s_word.neg_score())
  sorted_res = sorted(res.items(), key = lambda t : max(t[1][0], t[1][1]))
  sorted_res.reverse()
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
  if corpus_bool:
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
