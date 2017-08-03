import os
from user_param import class_name, test_path



def stats(result):
  data = 0
  good_classified = 0.
  n = len(class_name)
  for i in range(n):
    if os.path.isdir(test_path[i]):
      file_list = os.listdir(test_path[i])
      for f in file_list:
        if result[test_path[i] + f] == class_name[i]:
          good_classified += 1
        data += 1
    else:
      raise Exception('To be implemented...')

  print good_classified / data

