'''
Functions for handler utilities
'''

import random
import string

letters =  string.ascii_letters + string.digits

def random_key():
    '''Random key generation of 10 size length'''
    return ''.join(random.choice(letters) for i in range(10))


if __name__ == '__main__':
    print(random_key())