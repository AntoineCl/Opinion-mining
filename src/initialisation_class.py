from user_param import class_name

nbr_cl = len(class_name)
"""int: class number"""

class_dict = {}
"""dict: dictionary where each key is a name class and each value is an other
dictionary where a key is 'nbr_occ' and is associated value is the number of
documents in learning set for this class.
"""

sum_learning = 0
"""int: total number of documents in learning class"""

def initialize_class():
  """Initialize 'class_dict' with name of classes"""
  for cl in class_name:
    class_dict[cl] = {'nbr_occ': 0}

def add_count(cl, n):
  """Increases the occurence number of 'cl' class by 'n' and update also
  sum_learning.

  Parameters
  ----------

  Returns
  -------
  None
  """
  global sum_learning
  class_dict[cl]['nbr_occ'] += n
  sum_learning += n

def get_sum_learning():
  return sum_learning

