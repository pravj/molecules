#!/usr/bin/python
import os
import random
import string

thisfile = os.path.basename(__file__)

text_to_write = "tdy will be loved" # o.O
print text_to_write

random_word = ''.join(random.choice(string.ascii_lowercase) for i in range(3))

data = ''

with open(thisfile, 'r') as f:
        lines = f.readlines()
        f.close()

        lines[7] = lines[7].replace(lines[7][17:20], random_word)

        data = ''.join(lines)

with open(thisfile, 'w') as f:
        f.write(data)
        f.close()
