import time
def isValidParentheses(s):
    my_key = {'(': ')', '[': ']', '{': '}'}
    s_list = list(s)
    # print(s_list)
    stack = []
    for item in s_list:
        if item == '(' or item == '[' or item == '{':
            stack.append(item)
        elif stack:
            # print(item)
            if my_key[stack[-1]] == item:
                stack.pop()
            else:
                return False
        else:
            return False

    if stack:
        return False
    else:
        return True


s="[]{[]}[]["

start = time.clock()
a = isValidParentheses(s)
end = time.clock()
print("read: %f s" % (end - start))



print(a)