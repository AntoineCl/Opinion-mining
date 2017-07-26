from name_class import class_list

# vocabulary structure: {word : {classe1 : nbr_occ_in_classe1,
#                                classe2 : ...}}
vocabulary = {}
# global voc_size
voc_size = 0
intern_dico = {}

for name in class_list:
  intern_dico[name] = 0

# def initialize_voc():
  # to implement

from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

#~ wn_list = wn.all_lemma_names()
wn_list = wn.all_synsets()
swn_list = swn.all_senti_synsets()

stop = 100

voc = {}

def add_key(dico, key):
  global voc_size
  if key not in dico:
    dico[key] = intern_dico.copy()
    voc_size += 1

def condition_opscore(word, threshold):
  return word.pos_score() >= threshold or word.neg_score() >= threshold

def condition(word):
  # return condition_opscore(word, 0.2)
  return True

# return
def voc_basis_sentiword(): # sans pos tag mais avec la condition sur le score d'opinion
  i = 0
  for w in wn_list:
    # print w # w = la ref wordnet
    tmp = str(w.name()).split('.')
    # print tmp
    if len(tmp) >= 4:
      continue
    nam = tmp[0] # nam = le nom comme il est dans le texte
    # print nam

    if nam+'.x' in voc:
      continue

    # print list(swn.senti_synsets(nam))
    id_swn = list(swn.senti_synsets(nam))[0] # id_swn = la ref sentiword
    # print id_swn
    if condition(id_swn):
      add_key(voc, nam+'.x')
    i += 1
    print i
    if i == stop:
      break

def voc_pos_sentiword(): # avec pos tag et la condition sur le score d'opinion
  i = 0
  for w in wn_list:
    # print w # w = la ref wordnet
    tmp = str(w.name()).split('.')
    # print tmp
    if len(tmp) >= 4:
      continue # on ignore les cas particulier ou le nom contient un '.' par facilite
    nam = tmp[0] # nam = le nom comme il est dans le texte
    # print nam
    # print list(swn.senti_synsets(nam))

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

    # list_s = list(swn.senti_synsets(nam, 's')) # pas besoin car deja compris dans les adjective
    # if list_s != []:
      # id_swn_s = list_s[0]
      # if condition(id_swn_s):
        # add_key(voc, nam+'.s')

    # print list_n
    # print list_a
    # print list_v
    # print list_r

    i += 1
    # print i
    if i == stop:
      break



voc_basis_sentiword()
# voc_pos_sentiword()

# print voc
# print ''
# print voc_size











