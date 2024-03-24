class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,target,path):
            if target==0:
                res.append(path)
            if target<0:
                return
            for i in range(start,len(candidates)):
                backtrack(i,target-candidates[i],path+[candidates[i]])
        res =[]
        backtrack(0,target,[])
        return res
