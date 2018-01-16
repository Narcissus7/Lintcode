# coding=utf-8
"""
    给你一个 n 个整数的序列 a1,a2,...,an，一个 132 模式是对于一个子串 ai,aj,ak，满足 i < j < k 和 ai < ak < aj。
    设计一个算法来检查输入的这 n 个整数的序列中是否存在132模式。n 会小于 20,000。
    给你序列 nums = [1,2,3,4]
    返回 False//没有132模式在这个序列中。
    给你序列 nums = [3,1,4,2]
    返回 True//存在132模式：[1,4,2]。
"""

"""
    @param: nums: a list of n integers
    @return: true if there is a 132 pattern or false
"""


def find132pattern(nums):
    # write your code here

    for i in range(len(nums)-2):
        temp = [nums[i], nums[i+1], nums[i+2]]
        if nums[i] < nums[i+2] < nums[i+1]:
            return True
        else:
            continue

    return False


nums = [1,4,5,6,5]
print (find132pattern(nums))