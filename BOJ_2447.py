import sys
sys.setrecursionlimit(10**6)


def printStar(l):
    if l == 1:
        return ['*']

    star = printStar(l//3)
    tmp = []

    for s in star:
        tmp.append(s*3)
    for s in star:
        tmp.append(s+' '*(l//3)+s)
    for s in star:
        tmp.append(s*3)
    return tmp


n = int(input())
print('\n'.join(printStar(n)))
