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
        res_dict = {}

        for word in strs:
            word_split = sorted(list(word))
            if str(word_split) in res_dict:
                res_dict[str(word_split)].append(word)
            else:
                res_dict[str(word_split)] = [word]
        res_list = [val for val in res_dict.values()]
        return res_list


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

