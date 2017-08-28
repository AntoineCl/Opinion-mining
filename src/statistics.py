import os
from user_param import class_name, test_path
from initialisation_class import nbr_cl

def stats(result):
  """Return the ratio of documents properly classified

  Parameters
  ----------
  result : dict
    The dictionary returned by 'classification' method: the keys are paths of
    test set and values are their estimated classification.

  Returns
  -------
  float
  """
  data = 0
  good_classified = 0.
  for i in range(nbr_cl):
    if os.path.isdir(test_path[i]):
      file_list = os.listdir(test_path[i])
      for f in file_list:
        if result[test_path[i] + f] == class_name[i]:
          good_classified += 1
        data += 1
    else:
      filereader = open(test_path[i], 'r')
      line = filereader.readline()
      j = 1
      while line != '':
        if result[test_path[i] + '_line_' + str(j)] == class_name[i]:
          good_classified += 1
        data += 1
        j += 1
        line = filereader.readline()
      filereader.close()

  return good_classified / data

