"""
    快排
    给定一个未排序的整数数组，找到其中位数。
    中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。
    给出数组[4, 5, 1, 2, 3]， 返回 3
    给出数组[7, 9, 4, 5]，返回 5
"""
def median(nums):
    num = sorted(nums)
    if len(num)%2 == 0:
        res = num[len(num)//2-1]
    else:
        res = num[int(len(num)//2)]
    return res



nums = [4, 5, 1,2]
print(median(nums))