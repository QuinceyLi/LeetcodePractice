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
        # ！没有考虑全部情况
        # left, right = 0, len(nums)-1
        # sorted_nums = sorted(nums)
        # res = []
        # while right-left>=2 and sorted_nums[left]<=0 and sorted_nums[right]>=0:
        #     target_num = -sorted_nums[right]-sorted_nums[left]
        #     if target_num in sorted_nums[left+1:right]:
        #         if [sorted_nums[left],target_num,sorted_nums[right]] not in res:
        #             res.append([sorted_nums[left],target_num,sorted_nums[right]])
        #     if target_num<=0:
        #         right-=1
        #     else:
        #         left+=1
        # return res

        # if len(nums)<3:
        #     return []
        # idx = 0
        # sorted_nums = sorted(nums)
        # res = []
        # while sorted_nums[idx]<=0:
        #     left=idx+1
        #     right=len(nums)-1
        #     while left<right:
        #         if sorted_nums[idx]+sorted_nums[right]+sorted_nums[left]==0:
        #             res.append([sorted_nums[idx],sorted_nums[right],sorted_nums[left]])
        #         left+=1
        #         right-=1
        #     idx+=1
        # return res


        # 超时
        sorted_nums = sorted(nums)
        n_len=len(sorted_nums)
        res= []
        for idx in range(n_len-2):
            if sorted_nums[idx]==sorted_nums[idx-1] and idx>0:
                continue
            num_1 = sorted_nums[idx]
            if num_1>0:break

            r=n_len-1
            for l in range(idx+1,n_len-1):
                if sorted_nums[l]==sorted_nums[l-1] and l>idx+1:
                    continue

                # 参考答案版本
                # while r>l and sorted_nums[l]+sorted_nums[r]+num_1>0:
                #     r-=1
                # if r==l: break

                # if sorted_nums[l]+sorted_nums[r]+num_1==0:
                #     res.append([sorted_nums[l], sorted_nums[r], num_1])

                
                for r in range(l+1,n_len)[::-1]:
                    if sorted_nums[l]+sorted_nums[r]+num_1==0:
                        res.append([sorted_nums[l], sorted_nums[r], num_1])
                        break
                    elif sorted_nums[l]+sorted_nums[r]+num_1 <0: break
                    
        return res



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

