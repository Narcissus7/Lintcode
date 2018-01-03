stack1 = []
stack2 = []


"""
@param: element: An integer
@return: nothing
"""


def push(element):
    stack1.append(element)

    # write your code here


"""
@return: An integer
"""


def pop():
    # write your code here
    stack2 = stack1[::-1]
    print(stack2)
    if stack2:
        del stack1[0]
        return stack2.pop()
    else:
        return 0


"""
@return: An integer
"""


def top():
    if stack2:
        return stack1[-1]
    else:
        return 0


push(1)
# print(stack1[::-1])
a = pop()
print(a)
print(stack1,stack2)
push(2)
push(3)
b = top()
print(b)
c = pop()
print(c)


