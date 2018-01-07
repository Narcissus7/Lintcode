# import re   re好耗时
import time


def simplifyPath(path):
    # write your code here
    # path = re.sub('///', '/', path)
    # path = re.sub('//', ',', path)
    path = path.replace('///', '/')
    path = path.replace('//', ',')
    # print(path)
    if not path.endswith('/'):
        path = path + '/'
    path_list = path.split('/')
    # print(path_list)
    temp = path_list[-2]
    if (temp == '.') or (temp == '..'):
        res = '/'
    elif ('...' in temp) and (len(path_list) > 3):
        res = '/' + path_list[-3] + '/' + temp
    else:
        res = '/' + temp.replace(',', '/')

    return res


def simplifyPath1(path):

    path_array = path.split("/")
    stack = []
    res_path = ""
    for item in path_array:
        if item not in ["",".",".."]:
            stack.append(item)
        if ".." == item and stack:
            stack.pop(-1)
    if []==stack:
        return "/"
    for item in stack:
        res_path += "/"+item + ""
    return res_path


path = '/b//a/'

start = time.clock()
simplifyPath1(path)
end = time.clock()
print("read: %f s" % (end - start))

start = time.clock()
simplifyPath(path)
end = time.clock()
print("read: %f s" % (end - start))


# a = 'aaasss'
# a = a.replace('a', 's')
# print(a)
