import os
import re
import math
import random
import re
import sys


def pangrams(s):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    s = s.lower()

    for c in s:
        alphabet = alphabet.replace(c, '')



    if alphabet == '':
        return 'pangram'
    else:
        return 'not pangram'