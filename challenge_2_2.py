# Challenge 2.2
def solution(l):
    x= []
    y = []
    for item in l:
        x.append(list(map(int, item.split("."))))
    x.sort()
    for xtem in x:
        y.append(".".join(map(str, xtem)))
    print(",".join(y))