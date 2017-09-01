Introduction:
=============

This project implements a naive bayesian classifier for a particular type of
document classification: sentiment analysis (also called opinion mining).
If these notions are foreign to you, please look at
https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Document_classification
and
https://www.cs.cornell.edu/home/llee/papers/sentiment.pdf
for first concept.

Note that this project is intended to be an implementation of naive bayesian
classifier of this last paper.

Execution:
==========

Launch 'python src/main.py' with python 2.7 . If you want to launch from another
directory, make care to paths of data (see user parameters section below).

User parameters:
================

In the file 'src/user_param.py' you can find all parameters alterable by the
user. For example, there is 'class_name' variable that defines name of different
classes (here: 'positive' and 'negative').

Other variables are 'learning_path' and 'test_path' that represent respectively
the path of learning data set and the path of test data set. By default, these
are relative paths from root of the project, but you can use absolute path on
your computer.

To obtain good result, we recommend setting 'threshold' to 0.2 . Size of
vocabulary sould depend of corpus size. We recommend setting 'max_voc_size'
between 300 (for small learning set) and 5000 (for very big learning set). The
same you should activate 'corpus_bool' only with medium or big learning set.

More informations about user parameters in 'src/user_param.py'.

Data set:
=========

Currently there is one review in each class in data set to not overload this
repository.
You can find more data here:

https://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz

https://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz
This is data set mainly used to experiment precision of this project. We
recommend use it because it's larger.

External libraries:
===================

To run this project, you needs to external libraries:

numpy:
http://www.numpy.org/

nltk:
http://www.nltk.org/

text-unidecode:
https://pypi.python.org/pypi/text-unidecode/1.0


