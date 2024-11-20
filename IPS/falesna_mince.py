from math import ceil, log2

# simuluju cinknutou minci, kde s pravděpodobností p padne 1, 1-p 0
# p = a/b
def prumerny_pocet_hodu(a,b):
    return (1/(b/2**(ceil(log2(b)))))*ceil(log2(b))