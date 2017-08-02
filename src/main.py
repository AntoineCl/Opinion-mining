# encoding=utf8

from initialisation_class import initialize_class
print 'class imported'
from vocabulary import define_voc
print 'voc imported'
from learning_class import learning
print 'learning imported'
from bayes import classification
print 'classification imported'
from statistics import *

# bool_pos: bool
# threshold: float (score d'opinion entre 0. et 1., 0 pour pas de condition)
# pres_bool: bool True ssi on utilise la presence au lieu de la frequence (voir bayes.py)

def execute(bool_pos, threshold, pres_bool):

  initialize_class()
  print 'class initialized'

  voc = define_voc(bool_pos, threshold)
  print 'voc defined'

  learning(voc, bool_pos)
  print 'learning terminated'

  result = classification(voc, bool_pos, pres_bool)
  print 'classification terminated'

  print result
  print ""
  # return result

  stats(result)

if __name__ == '__main__':
  execute(False, 0.0, False)
  # execute(True, 0., False)

# faire fonction qui supprime les .directory des ensemble d'apprentissage
