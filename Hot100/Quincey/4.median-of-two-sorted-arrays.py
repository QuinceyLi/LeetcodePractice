# @lcpr-before-debug-begin
from python3problem4 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    flag = False if l == len(nums) or nums[l] != target else True
    return l, flag
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0: return nums2[n2 // 2] if n2%2 == 1 else (nums2[n2//2] + nums2[n2//2+1])/2
        elif n2 == 0: return nums1[n1 // 2] if n1%2 == 1 else (nums1[n1//2] + nums1[n1//2+1])/2
        ans = [-1] * (n1+n2)
        mid_loc = [(n1+n2) // 2] if (n1+n2) % 2 == 1 else [(n1+n2) // 2 -1, (n1+n2) // 2]
        acur, ncur, i = 0, 0, 0
        while acur <= max(mid_loc):
            loc,bool_flag = lower_bound(nums1[ncur:], nums2[i])
            if bool_flag: 
                ans[acur:acur+loc+1], ans[acur+loc+1] = nums1[ncur:ncur+loc+1], nums2[i]
                acur += loc + 2
                
            else: 
                ans[acur:acur+loc], ans[acur+loc] = nums1[ncur:ncur+loc], nums2[i]
                acur += loc + 1
            ncur += loc + 1
            i += 1
        return sum([ans[x] for x in mid_loc])/len(mid_loc)
        # if len(a) > len(b):
        #     a, b = b, a  # 保证下面的 i 可以从 0 开始枚举

        # m, n = len(a), len(b)
        # a = [-inf] + a + [inf]
        # b = [-inf] + b + [inf]

        # # 枚举 nums1 有 i 个数在第一组
        # # 那么 nums2 有 (m + n + 1) // 2 - i 个数在第一组
        # i, j = 0, (m + n + 1) // 2
        # while True:
        #     if a[i] <= b[j + 1] and a[i + 1] > b[j]:  # 写 >= 也可以
        #         max1 = max(a[i], b[j])  # 第一组的最大值
        #         min2 = min(a[i + 1], b[j + 1])  # 第二组的最小值
        #         return max1 if (m + n) % 2 else (max1 + min2) / 2
        #     i += 1  # 继续枚举
        #     j -= 1


# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,4,4]\n[2,2,2,4,4]\n
# @lcpr case=end

#

