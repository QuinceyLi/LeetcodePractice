#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 类似于栈的思想，但是判断进出有问题，没有考虑到右边接不住水的情况
        # temp_list = []
        # total_water = 0
        # left = height[0]
        # height.pop(0)
        # while height:
        #     temp_list.append(height.pop(0))
            
        #     if height == [] or (temp_list and left <= temp_list[-1]):
        #         if len(temp_list)>1:
        #             # print(f"left: {left},  temp: {temp_list}")
        #             max_h = max(temp_list)
        #             if left > max_h:
        #                 if temp_list[0]==max_h:
        #                     left = max(temp_list[1:])
        #                     temp_list = temp_list[1:]
        #                 else:
        #                     left = max(temp_list)

        #             for h in temp_list[:-1]:
        #                 total_water+=left-h
                
        #         left = temp_list[-1]
        #         temp_list = []
        #     # print(f"height: {height}")
        # return total_water


    #--------------看了参考答案后自己写-----------
        # # 动态规划
        # leftmax,rightmax = [], []
        # max_left = height[0]
        # for i in range(1,len(height)-1):
        #     max_left = max(max_left,height[i])
        #     leftmax.append(max_left-height[i])

        # max_right = height[-1]
        # for j in range(1,len(height)-1)[::-1]:
        #     max_right = max(max_right,height[j])
        #     rightmax.append(max_right - height[j])
        # rightmax = rightmax[::-1]
        
        # return sum([min(leftmax[n],rightmax[n]) for n in range(0,len(leftmax))])

    # 双指针
        left,right = 0,len(height)-1
        l_max, r_max =0,0
        total_water = 0
        while left<right:
            l_max = max(l_max,height[left])
            r_max = max(r_max,height[right])
            if l_max < r_max:
                total_water += l_max- height[left]
                left +=1
            else:
                total_water += r_max - height[right]
                right -= 1
        return total_water
            
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

