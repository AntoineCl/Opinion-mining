from name_class import class_list

from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

wn_list = wn.all_synsets()
swn_list = swn.all_senti_synsets()

intern_dico = {}

for name in class_list:
  intern_dico[name] = 0


stop = 1000
# stop = 1500000

def add_key(dico, key):
  global voc_size
  if key not in dico:
    dico[key] = intern_dico.copy() # on initialise les occurence a zero
    # voc_size += 1

def voc_count_one(voc, word, classname):
  voc[word][classname] += 1 # on met a jour les occurence de vocabulaire

def condition_opscore(word, threshold):
  if threshold == 0.:
    return True
  else:
    return word.pos_score() >= threshold or word.neg_score() >= threshold

# return
def voc_basis_sentiword(threshold): # sans pos tag mais avec la condition sur le score d'opinion
  voc = {}
  i = 0
  for w in wn_list:
    tmp = str(w.name()).split('.')
    if len(tmp) >= 4:
      continue
    nam = tmp[0] # nam = le nom comme il est dans le texte
    if nam+'.x' in voc:
      continue
    id_swn = list(swn.senti_synsets(nam))[0] # id_swn = la ref sentiword
    if condition_opscore(id_swn, threshold):
      add_key(voc, nam + '.x')
    i += 1
    # print i
    if i == stop:
      break
  return voc

def voc_pos_sentiword(threshold): # avec pos tag et la condition sur le score d'opinion
  voc = {}
  i = 0
  for w in wn_list:
    tmp = str(w.name()).split('.')
    if len(tmp) >= 4:
      continue # on ignore les cas particulier ou le nom contient un '.' par facilite
    nam = tmp[0] # nam = le nom comme il est dans le texte
    if nam+'.n' in voc or nam+'.a' in voc or nam+'.v' in voc or nam+'.r' in voc:
      continue

    list_n = list(swn.senti_synsets(nam, 'n'))
    if list_n != []:
      id_swn_n = list_n[0]
      if condition_opscore(id_swn_n, threshold):
        add_key(voc, nam+'.n')

    list_a = list(swn.senti_synsets(nam, 'a'))
    if list_a != []:
      id_swn_a = list_a[0]
      if condition_opscore(id_swn_a, threshold):
        add_key(voc, nam+'.a')

    list_v = list(swn.senti_synsets(nam, 'v'))
    if list_v != []:
      id_swn_v = list_v[0]
      if condition_opscore(id_swn_v, threshold):
        add_key(voc, nam+'.v')

    list_r = list(swn.senti_synsets(nam, 'r'))
    if list_r != []:
      id_swn_r = list_r[0]
      if condition_opscore(id_swn_r, threshold):
        add_key(voc, nam+'.r')

    i += 1
    # print i
    if i == stop:
      break
  return voc

# voc structure: {word : {classe1 : nbr_occ_in_classe1, classe2 : ...}, ...}
def define_voc(bool_pos, threshold):
  if bool_pos:
    return voc_pos_sentiword(threshold)
  else:
    return voc_basis_sentiword(threshold)


def get_voc_count(voc, word, classname):
  return voc[word][classname]









