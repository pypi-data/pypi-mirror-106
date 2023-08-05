import re

def single_spaced(x):
    return(re.sub(' +', ' ', x))
