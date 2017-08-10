"""This file contains all user parameters.
"""

class_name = ['positive', 'negative']
"""list: list of names class
"""

bool_pos = False
"""bool: boolean variable to determine if part-of-speech (POS) tagger is used
"""

threshold = 0.
"""float: minimum value of opinion score for selection words for vocabulary
construction
"""

# to delete for final version
stop = 1000

pres_bool = False
"""bool: True iff the presence method is used instead of frequency method
(see bayes.py)
"""

learning_path = [
                  '../data/learning_set/pos/',
                  '../data/learning_set/neg/'
                ]
"""list: list of learning sets paths.
WARNING: path in same order than class_name
"""

test_path = [
              '../data/test_set/pos/',
              '../data/test_set/neg/'
            ]
"""list: list of test sets paths.
WARNING: path in same order than class_name
"""


