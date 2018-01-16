import time


def expressionExpand(s):
    stack = []
    slist = list(s)
    for i in range(len(slist)):
        if slist[i].isdigit() and slist[i + 1].isdigit():
            slist[i + 1] = slist[i] + slist[i + 1]
            slist[i] = ""
    if "" in slist:
        slist.remove("")
    # print(slist)

    for st in slist:
        if st != ']':
            stack.append(st)
        else:
            tempstr = []
            while stack[-1] != '[':
                tempstr.append(stack.pop())
                # print(tempstr)
            stack.pop()
            tempstr = "".join(tempstr[::-1])
            tempnum = int(stack.pop())
            # print(tempnum)
            stack.append(tempstr * tempnum)

    res = "".join(stack)
    # print(slist)
    return res


s = 'abc3[a]w'
ss = '300[2[ad]3[pf]]xyz'
a = "203[a]"

start = time.clock()
print (expressionExpand(ss))
end = time.clock()
print("read: %f s" % (end - start))
