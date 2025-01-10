#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30204
#
# [207] 课程表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #BFS
        # from collections import deque
        # indegrees = [0 for _ in range(numCourses)]
        # adjacency = [[] for _ in range(numCourses)]
        # queue = deque()
        # for cur, pre in prerequisites:
        #     indegrees[cur] += 1
        #     adjacency[pre].append(cur)
        # for i in range(numCourses):
        #     if not indegrees[i]: queue.append(i)
        # while queue:
        #     pre = queue.popleft()
        #     numCourses -= 1
        #     for cur in adjacency[pre]:
        #         indegrees[cur] -= 1
        #         if not indegrees[cur]: queue.append(cur)
        # return not numCourses

        #DFS
        def dfs(i,adjacency,flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True
        
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#

