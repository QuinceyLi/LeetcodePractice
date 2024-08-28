#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 看错题了，子数组的定义没看到
        # sum_dict = {}
        # for i in range(len(nums)):
        #     total_list_to_sum = [int(x) for x in sum_dict.keys()]
        #     for n in total_list_to_sum:
        #         temp_sum = nums[i]+n
        #         temp_sum_list = sum_dict.get(str(n),[[]])
        #         if temp_sum == nums[i]:
        #             new_sum_list = [[nums[i]]+x for x in temp_sum_list]
        #         new_sum_list = [[nums[i]]+x for x in temp_sum_list]
        #         sum_dict[str(temp_sum)] = new_sum_list + sum_dict.get(str(temp_sum),[])
        #     if str(nums[i]) not in sum_dict:
        #         sum_dict[str(nums[i])]=[[nums[i]]]  
        #     else:
        #         sum_dict[str(nums[i])].append([nums[i]])
        #     print(i,sum_dict)  
        # return len(sum_dict.get(str(k),[]))


        # total_counts = 0
        # for i in range(len(nums)):
        #     j=i+1
        #     while j<len(nums) and sum(nums[i:j])!=k:
        #         j+=1
        #     # print(i,j,nums[i:j])
        #     if sum(nums[i:j])==k:
        #         total_counts+=1
        #         p=j
        #         while p<len(nums):
        #             # print(p,nums[p])
        #             if nums[p]==0:
        #                 total_counts+=1
        #                 p+=1

        #             else:
        #                 break
        # return total_counts

        # 优化第一种思路
        # sum_dict = {0:0}
        # for i in range(len(nums)):
        #     sum_dict_1=sum_dict.copy()
        #     for key,value in sum_dict_1.items():
        #         temp_sum = nums[i]+value
        #         sum_dict[temp_sum]=sum_dict.get(temp_sum,0)+1
        #     # sum_dict[temp_sum]=sum_dict.get(temp_sum,0)+1

        # return sum_dict.get(k,0)

            
        # 参考答案
        total_counts = 0
        pre_sum =0
        sum_dict = {0:1}
        for i in range(len(nums)):
            pre_sum = pre_sum + nums[i]
            total_counts += sum_dict.get(pre_sum-k,0)
            sum_dict[pre_sum] = sum_dict.get(pre_sum,0)+1
        return total_counts
        

# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

