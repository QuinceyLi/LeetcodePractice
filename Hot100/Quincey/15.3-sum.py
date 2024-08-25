#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if (nums[0] > 0) or (nums[-1] < 0 ):
            return []
        tylist = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[right] < 0:
                    break
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    temp = [nums[i],nums[left],nums[right]]
                    if sorted(temp) not in tylist:
                        tylist.append(temp)
                    left += 1
                    right -= 1

        return tylist
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

