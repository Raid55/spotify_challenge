# this is without the characters that dont appear in t
def sortByStrings(s, t):
    return "".join([l * s.count(l) for l in t])

# this is just in case I need to include the characters that arent included in t but that are in s
def sortByStringsWithRest(s, t):
    return "".join([l * s.count(l) for l in t] + [l for l in s if l not in t])
