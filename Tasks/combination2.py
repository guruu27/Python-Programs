class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,target,path):
            if target==0:
                res.append(path)
            if target<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                backtrack(i+1,target-candidates[i],path+[candidates[i]])
        res = []
        stack = []
        backtrack(0,target,[])
        if res:
            for i in res:
                i.sort()
                if i in stack:
                    continue
                stack.append(i)
        return stack
