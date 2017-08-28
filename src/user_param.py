bool_pos = False
"""bool: boolean variable to determine if part-of-speech (POS) tagger is used"""

threshold = 0.2
"""float: minimum value of opinion score for selection words for vocabulary
construction
"""

max_voc_size = 3000
"""int: desired vocabulary size"""

pres_bool = False
"""bool: True iff the presence method is used instead of frequency method
(see bayes.py)
"""

learning_path = [
                  '../data/learning_set/pos/',
                  '../data/learning_set/neg/'
                  # '../data/learning_set/pos.txt',
                  # '../data/learning_set/neg.txt'
                ]
"""list: list of learning sets paths.
WARNING: path in same order than class_name
"""

test_path = [
              '../data/test_set/pos/',
              '../data/test_set/neg/'
              # '../data/test_set/pos.txt',
              # '../data/test_set/neg.txt'
            ]
"""list: list of test sets paths.
WARNING: path in same order than class_name
"""

