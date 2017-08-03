class_name = ['positive', 'negative']

# boolean POS tag
bool_pos = False

# float, threshold of minimal of opinion score for vocabulary
threshold = 0.

#int, number of iteration in wordnet
stop = 1000

# boolean, True iff the presence method is used instead of frequency method (see bayes.py)
pres_bool = False

# warning: path in same order than class_name
learning_path = [
                  '../data/learning_set/pos/',
                  '../data/learning_set/neg/'
                ]


# warning: path in same order than class_name
test_path = [
              '../data/test_set/pos/',
              '../data/test_set/neg/'
            ]




