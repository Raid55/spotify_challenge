import re

# This took a little while but after a friend talked about eval it made sense to me, I was
# going for a recursive function at first since I had the regex working but it was hard
# after thinking about eval and pythons ability to do 5 * str it became evident and i filled in the gap
def decodeString(s):
    matches = re.findall(r'\d{1}\[[a-zA-Z]+', s)
    finalArr = []
    for pat in matches:
        finalArr.append(pat[0] + "*(" + '"' + pat[2:] + '"')
    return eval("+".join(finalArr) + ")" * len(matches))
