from user_param import class_name

nbr_cl = len(class_name)
"""int: Number of classes"""

class_dict = {}
"""dict: Dictionary where each key is a name class and each value is an other
dictionary where keys are 'nbr_occ' and 'voc_occ' and their associated value are
respectively the number of documents in learning set for this class and the
number (with occurrence) of vocabulary words appearing in this class.
"""

sum_learning = 0
"""int: Total number of documents in learning class"""

def initialize_class():
  """Initialize 'class_dict' with name of classes and a under-dictionary.

  nbr_occ is the number of documents in class 'cl' learning set,
  voc_occ is the sum of occurrence of vocabulary words in class 'cl' learning
  set.
  """
  for cl in class_name:
    class_dict[cl] = {'nbr_occ': 0,
                      'voc_occ': 0}

def add_count(cl, n):
  """Increases the occurrence number of 'cl' class by 'n' and update also
  sum_learning.

  Parameters
  ----------
  cl : str
    A name class
  n : int

  Returns
  -------
  None
  """
  global sum_learning
  class_dict[cl]['nbr_occ'] += n
  sum_learning += n

def get_sum_learning():
  """Return sum_learning"""
  return sum_learning

