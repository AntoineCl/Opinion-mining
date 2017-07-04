from name_class import class_list

nbr_cl = len(class_list)
class_dico = {}
sum_learning = 0

def initialize_class():
  for cl in class_list:
    class_dico[cl] = {'nbr_occ': 0}

# return the number of document of learning set
def update_sum_learning():
  x = 0
  for values in class_dico.values():
    x += values['nbr_occ']
  if x != sum_learning:
    raise Exception('Problem of counting of learning document')
  return x

if __name__ == '__main__':
  initialize_class()
