# coding=utf-8
"""
    快速排序
    在数组中找到第k大的元素
    给出数组 [9,3,2,4,8]，第三大的元素是 4
    给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推
"""

def kthLargestElement(k, A):
    B = sorted(A, reverse=True)

    return B[k-1]


A = [9,3,2,4,8]
k=3
print(kthLargestElement(k, A))