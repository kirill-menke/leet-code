class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res


    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        else:
            for i in range(index, len(candidates)):
                self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)