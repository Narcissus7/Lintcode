# from __future__ import division
import time
import math
def evalRPN(tokens):
    stack = []
    for item in tokens:
        if item.lstrip('-').isdigit():
            stack.append(item)
            res = eval(item)
        else:
            # res = 0
            a = str(stack.pop())
            b = str(stack.pop())
            # temp = '(' + b + ')' + item + '(' + a + ')'
            temp = b + item + a
            res = math.trunc(eval(temp))
            # if item == '/' and res < 0 and eval(b + "%" + a) != 0:   # py2需要
            #     res += 1
            stack.append(res)
    print(res)


tokens = ["6", "-132", "/"]

start = time.clock()
evalRPN(tokens)
end = time.clock()
print("read: %f s" % (end - start))

