# Challenge 2.1
def solution(l, t):
    j = 0
    found = 0
    for i, item in enumerate(l):
        if found == 1:
            break
        sum_index = []
        sum = item
        if sum == t:
            sum_index.append(i)
            found = 1
            print("%d,%d" % (sum_index[0], sum_index[-1]))
            break
        j = i+1
        sum_index.append(i)
        while sum < t:
            if j == len(l):
                break
            sum = sum + l[j]
            sum_index.append(j)

            j += 1
            if sum == t:
                found = 1
                print("%d,%d" % (sum_index[0], sum_index[-1]))

    if found == 0:
        print(",".join(map(str, [-1,-1])))