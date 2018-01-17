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

    if nums:
        stack = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] >= stack[0] and nums[i] >= stack[-1]:
                stack.append(nums[i])
            else:
                if nums[i] > min(stack):
                    return True
                else:
                    stack.append(nums[i])
    return False


nums = [1,4,5,6,5]
print (find132pattern(nums))