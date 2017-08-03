from user_param import class_name

nbr_cl = len(class_name)
class_dico = {}
sum_learning = 0

def initialize_class():
  for cl in class_name:
    class_dico[cl] = {'nbr_occ': 0}

def add_count(cl, n):
  global sum_learning
  class_dico[cl]['nbr_occ'] += n
  sum_learning += n

def get_sum_learning():
  return sum_learning

