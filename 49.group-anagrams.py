#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        while len(strs) > 0: # 用for str1 in strs,strs=['bat']的时候迭代停止
            str1 = strs[0]
            tempset = set(str1)
            templs = [str1]            
            strs.remove(str1)
            for str2 in strs:
                if set(str2)==tempset:
                    templs.append(str2)
                    strs.remove(str2)
            res.append(templs)
        return res
# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

