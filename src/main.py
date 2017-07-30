# encoding=utf8

from initialisation_class import initialize_class
print 'class imported'
from vocabulary import define_voc
print 'voc imported'
from learning_class import learning
print 'learning imported'
from bayes import classification
print 'classification imported'


initialize_class()
print 'class initialized'

define_voc()
print 'voc defined'

learning()
print 'learning terminated'

result = classification()
print 'classification terminated'

print '########################################'

print result


# mettre bool_pos dans un fichier modifiable par l'utilisateur
# faire fonction qui supprime les .directory des ensemble d'apprentissage
