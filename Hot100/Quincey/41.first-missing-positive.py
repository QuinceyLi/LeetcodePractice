#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n):
        #     # 将 nums[i] 放置到正确的位置上
        #     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # # 查找第一个位置 i 使得 nums[i] != i + 1
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1
        
        # return n + 1
        n = len(nums)
        nums.append(n + 1)
        # 将所有非正数改为 n
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n  + 1

        for i in range(n):
            x = abs(nums[i])
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])  # 打上标记
        for i, x in enumerate(nums):
            if x > 0:
                return i + 1

# @lc code=end



#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

