from user_param import class_name, bool_pos, threshold, stop
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

# voc structure: {word : {classe1 : nbr_occ_in_classe1,
#                                classe2 : ...}}

wn_list = wn.all_synsets()
swn_list = swn.all_senti_synsets()


voc = {}
voc_size = 0
intern_dico = {}

def init_intern_dico():
  for name in class_name:
    intern_dico[name] = 0


def add_key(dico, key):
  global voc_size
  if key not in dico:
    dico[key] = intern_dico.copy() # on initialise les occurence a zero
    voc_size += 1

def voc_count_one(word, classname):
  voc[word][classname] += 1 # on met a jour les occurence de vocabulaire

def condition_opscore(word, threshold):
  if threshold == 0:
    return True
  else:
    return word.pos_score() >= threshold or word.neg_score() >= threshold

def condition(word):
  return condition_opscore(word, threshold)

# return
def voc_basis_sentiword(): # sans pos tag mais avec la condition sur le score d'opinion
  i = 0
  for w in wn_list:
    tmp = str(w.name()).split('.')
    if len(tmp) >= 4:
      continue
    nam = tmp[0] # nam = le nom comme il est dans le texte
    if nam+'.x' in voc:
      continue
    id_swn = list(swn.senti_synsets(nam))[0] # id_swn = la ref sentiword
    if condition(id_swn):
      add_key(voc, nam + '.x')
    i += 1
    # print i
    if i == stop:
      break

def voc_pos_sentiword(): # avec pos tag et la condition sur le score d'opinion
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
      if condition(id_swn_n):
        add_key(voc, nam+'.n')

    list_a = list(swn.senti_synsets(nam, 'a'))
    if list_a != []:
      id_swn_a = list_a[0]
      if condition(id_swn_a):
        add_key(voc, nam+'.a')

    list_v = list(swn.senti_synsets(nam, 'v'))
    if list_v != []:
      id_swn_v = list_v[0]
      if condition(id_swn_v):
        add_key(voc, nam+'.v')

    list_r = list(swn.senti_synsets(nam, 'r'))
    if list_r != []:
      id_swn_r = list_r[0]
      if condition(id_swn_r):
        add_key(voc, nam+'.r')

    i += 1
    # print i
    if i == stop:
      break

def define_voc():
  init_intern_dico()
  if bool_pos:
    voc_pos_sentiword()
  else:
    voc_basis_sentiword()
  print voc_size

def get_voc():
  return voc

def get_voc_size():
  return voc_size

def get_voc_count(word, classname):
  return voc[word][classname]

# voc_basis_sentiword()
# voc_pos_sentiword()








