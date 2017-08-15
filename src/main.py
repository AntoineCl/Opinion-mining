#!/usr/bin/env python
#-*- coding: utf-8 -*-

def execute():
  """Main function of project. Uses other methods for classify test set.

  Parameters
  ----------

  Returns
  -------
  None
  """
  initialize_class()

  define_voc()
  print 'voc define'

  learning()
  print 'end learning'

  result = classification()
  # print result
  print ""

  print stats(result)

if __name__ == '__main__':
  from initialisation_class import initialize_class
  from vocabulary import define_voc
  from learning_class import learning
  from bayes import classification
  from statistics import stats

  execute()

