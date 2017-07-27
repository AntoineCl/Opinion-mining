import os
import nltk

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


# input: bool_pos: boolean true iff pos tag is activated
def formatting(tokens, bool_pos):
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


# input: filename : absolute path
def tokenize_file(filename, bool_pos):
  filereader = open(filename, 'r')
  string = filereader.read()
  filereader.close()
  tokens = nltk.word_tokenize(string)
  # print tokens
  newtokens = formatting(tokens, bool_pos)
  # print newtokens
  return newtokens



sentence = "At eight o'clock on Thursday morning, Arthur didn't feel very good and Jesus is a good god. The dog is going to eat. I'm angry. The car I've bought is red."

tokens = nltk.word_tokenize(sentence)
# print tokens



formatting(tokens, False)
formatting(tokens, True)

# tokenize_file('/home/antoine/documents/tmp/tmp1.txt', False)
# tokenize_file('/home/antoine/documents/tmp/tmp1.txt', True)
