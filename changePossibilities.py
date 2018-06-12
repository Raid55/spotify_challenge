from collections import Counter
from copy import copy

# This still needs some work and doesen't work entirely, I will keep updating it when I get it to work
# with any permutations... will work on it
def changePossibilities(amount, denom):
    posib = 0
    alredy = []
    denom = list(set(denom))
    for d in denom:
        if d == amount:
            posib += 1
            continue;
        elif d > amount:
          continue;
        to = [d]
        for test in denom:
            while sum(to) < amount:
                to.append(test)
                if sum(to) == amount and notAlredy(alredy, to):
                    print(to)
                    print("")
                    alredy.append(copy(to))
                    posib += 1
            del to[1:]
    return posib

def notAlredy(a, c):
  for l in a:
    if Counter(l) == Counter(c):
      return False
  return True

