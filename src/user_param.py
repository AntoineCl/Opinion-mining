"""This file contains all user parameters."""

class_name = ['positive', 'negative']
"""list: list of names class"""

pos_bool = False
"""bool: boolean variable to determine if part-of-speech (POS) tagger is used"""

corpus_bool = False
"""bool: boolean to determine if vocabulary is based on frequent opinion words
in learning set.
"""

threshold = 0.2
"""float: Minimum value of opinion score of selected words for vocabulary
construction. This value is between 0.0 and 1.0
"""

max_voc_size = 3000
"""int: maximum vocabulary size"""

pres_bool = False
"""bool: True iff the presence method is used instead of frequency method
(see bayes.py)
"""

learning_path = [
                  'data/learning_set/pos/',
                  'data/learning_set/neg/'
                  # 'data/learning_set/pos.txt',
                  # 'data/learning_set/neg.txt'
                ]
"""list: list of learning sets paths.
WARNING: paths in same order than class_name
"""

test_path = [
              'data/test_set/pos/',
              'data/test_set/neg/'
              # 'data/test_set/pos.txt',
              # 'data/test_set/neg.txt'
            ]
"""list: list of test sets paths.
WARNING: paths in same order than class_name
"""
