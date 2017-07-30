# encoding=utf8

from initialisation_class import initialize_class
print 'class imported'
from vocabulary import define_voc
print 'voc imported'
from learning_class import learning
print 'learning imported'

print 'bbbbbbbbbbbbbbbbbbbbbbbbb_first_main'

initialize_class()

define_voc(False)

learning(False)




# mettre bool_pos dans un fichier modifiable par l'utilisateur
# faire fonction qui supprime les .directory des ensemble d'apprentissage
