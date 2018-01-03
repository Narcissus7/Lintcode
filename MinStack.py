my_stack = []
"""
@param: number: An integer
@return: nothing
"""


def push(number):
    my_stack.append(number)


"""
@return: An integer
"""


def pop():
    # write your code here
    if my_stack:
        return my_stack.pop()
    else:
        return 0


"""
@return: An integer
"""


def my_min():
    try:
        map(int, my_stack)
        return min(my_stack)
    except:
        return 0

push(1)
print(pop())
print(my_stack)
push(2)
push(3)
print(my_stack)
print(my_min())
push(1)
print(my_min())