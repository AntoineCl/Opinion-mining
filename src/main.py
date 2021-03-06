def execute():
  """Main function of project. Uses other methods for classify test set."""
  initialize_class()
  define_voc()
  learning()
  result = classification()
  stat = stats(result)
  print 'Ratio of documents well classified : ' + str(stat)

if __name__ == '__main__':
  from initialisation_class import initialize_class
  from vocabulary import define_voc
  from learning_class import learning
  from bayes import classification
  from statistics import stats

  execute()

