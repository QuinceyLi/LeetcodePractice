#
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30204
#
# [189] 轮转数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        real_k = k%n
        nums[:n-real_k] = nums[:n-real_k][::-1]
        nums[n-real_k:n] = nums[n-real_k:n][::-1]

        nums.reverse()
        # print(nums)
        return nums
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-100,3,99]\n2\n
# @lcpr case=end

#

