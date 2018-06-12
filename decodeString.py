import re

def decodeString(s):
    matches = re.findall(r'\d{1}\[[a-zA-Z]+', s)
    finalArr = []
    for pat in matches:
        finalArr.append(pat[0] + "*(" + '"' + pat[2:] + '"')
    return eval("+".join(finalArr) + ")" * len(matches))
