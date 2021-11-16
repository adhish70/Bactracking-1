# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

# Time Complexiety: O(n*(2^n))
# Space Complexiety: O(n)

class Solution:
    def __init__(self):
        self.result = list()
        
    def _helper(self, candidates, target, idx, cur, path):
        # Base condition
        if idx == len(candidates):
            return
        
        if cur > target:
            return
        
        if cur == target:
            self.result.append(path.copy())
        
        n = len(candidates)
        for i in range(idx, n):
            # action
            path.append(candidates[i])
            cur += candidates[i]
            
            # recursion
            self._helper(candidates, target, i, cur, path)
            
            # backtrack
            cur -= candidates[i]
            path.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self._helper(candidates, target, 0, 0, [])
        return self.result