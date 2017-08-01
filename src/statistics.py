import os
from test_set import test_path
from name_class import class_list



def stats(result):
  data = 0
  good_classified = 0
  n = len(class_list)
  for i in range(n):
    if os.path.isdir(test_path[i]):
      file_list = os.listdir(test_path[i])
      for f in file_list:
        if result[test_path[i] + f] == class_list[i]:
          good_classified += 1
        data += 1
    else:
      print 'to be implemented (stats() in statistics.py)'

  print float(good_classified) / data

# modifier code pour mettre en parametre:
  # presence ou frequence
  # avec ou sans POS tag
  # vocubulaire:
    # nbr mot
    # score d'opinion si necessaire
  # ensemble d'apprentissage et d'entrainement
