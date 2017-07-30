import os
import nltk
from pos_tag import bool_pos

# rename the pos tag of nltk for sentiword
pos_conversion = {
                  'ADJ': 'a',
                  # 'ADP': ,
                  'ADV': 'r',
                  # 'CONJ': ,
                  # 'DET': ,
                  'NOUN': 'n',
                  # 'NUM': ,
                  # 'PRT': ,
                  # 'PRON': ,
                  'VERB': 'v',
                  # '.': ,
                  # 'X': ,
                  }


def formatting(tokens):
  # print tokens
  if not bool_pos:
    newtokens = list(map(lambda t : t + '.x', tokens))
  else:
    newtokens = []
    tagged = nltk.pos_tag(tokens, 'universal')
    # print tagged
    # newtokens = list(map(lambda (a, b) : (a, pos_conversion[b]), tagged)) # on ne sait pas si b existe
    n = len(tagged)
    for i in range(n):
      if tagged[i][1] in pos_conversion:
        newtokens += [tagged[i][0] + '.' + pos_conversion[tagged[i][1]]]
        # print newtokens
  # print newtokens
  return newtokens

def tokenize_string(string):
  tokens = nltk.word_tokenize(string)
  # print tokens
  newtokens = formatting(tokens)
  # print newtokens
  return newtokens

# input: filename : absolute path
def tokenize_file(filename):
  print 'tokenize : ' + filename
  filereader = open(filename, 'r')
  string = filereader.read()
  filereader.close()
  tokens = tokenize_string(string)
  return tokens



# sentence = "At eight o'clock on Thursday morning, Arthur didn't feel very good and Jesus is a good god. The dog is going to eat. I'm angry. The car I've bought is red."

# tokens = nltk.word_tokenize(sentence)
# print tokens


