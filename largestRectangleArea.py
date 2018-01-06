import time
# def largestRectangleArea(height):
#     print(time.strftime('%H:%M:%S', time.localtime(time.time())))
#     # write your code here
#     res = []
#     area = 0
#     length = len(height)
#     if height:
#         for i in range(len(height)):
#             temp_width = 1
#             temp_height = height[i]
#             res.append(height[i] * 1)
#             for j in range(i+1, length):
#                 temp_width += 1
#                 if height[j] < temp_height:
#                     temp_height = height[j]
#                 temp_area = temp_height * temp_width
#                 if temp_area > area:
#                     area = temp_area
#         res.append(area)
#         print(max(res),res)
#         print(time.strftime('%H:%M:%S', time.localtime(time.time())))
#     else:
#         print(0)

# def largestRectangleArea(height):
#     print(time.strftime('%H:%M:%S', time.localtime(time.time())))
#     sort_height = sorted(list(set(height)))
#     print(time.strftime('%H:%M:%S', time.localtime(time.time())))
#     # print(sort_height)
#     height.append(0)
#     height.insert(0, 0)
#     # print(height)
#     area = 0
#     res = []
#     res.append(area)
#     for i in range(len(sort_height)):
#         index_0 = [j for j, a in enumerate(height) if a == 0]
#         index_temp = [j for j, a in enumerate(height) if a == sort_height[i]]
#         # print(index_0)
#         temp_h = sort_height[i]
#         for k in range(len(index_0)-1):
#             temp_w = index_0[k+1] - index_0[k] - 1
#             temp_area = temp_h * temp_w
#             if temp_area > area:
#                 area = temp_area
#             # print(height)
#         for num in index_temp:
#             height[num] = 0
#         # print(height)
#     res.append(area)
#
#     print(max(res), res)
#     print(time.strftime('%H:%M:%S', time.localtime(time.time())))
        # temp_w =

def largestRectangleArea(height):
    res = []
    stack = []
    stacklen = 0
    area = 0
    height.append(0)
    for i in range(len(height)):
        if (not stack) or (height[stack[-1]] <= height[i]):
            stack.append(i)
        else:
            if len(stack) > stacklen:
                stacklen = len(stack)
            tmp_index = stack.pop()
            if not stack:
                temp_area = i * height[tmp_index]
            else:
                temp_area = (i - stack[-1] - 1) * height[tmp_index]
                # print(i, height[tmp_index])
            if temp_area > area:
                area = temp_area
        res.append(area)
    print(max(res), res)


# def largestRectangleArea(height):
#     maxArea = 0
#     stack = []
#     height.append(0)
#     length = len(height)
#     for i in range(length):
#         if i == length:
#             nowh = 0
#         else:
#             nowh = height[i]
#
#         while (stack) and (nowh <= height[stack[-1]]):
#             h = height[stack[-1]]
#             stack.pop()
#             if not stack:
#                 w = i
#             else:
#                 w = i - 1 - stack[-1]
#             area = w * h
#             maxArea = max(maxArea, area)
#
#         stack.append(i)
#
#     print(maxArea)

largestRectangleArea([5,5,6,6,4,4])
largestRectangleArea([2,1,5,6,2,3])

