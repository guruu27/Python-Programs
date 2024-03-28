class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def backtrack(nums,path):
            if path not in res and not nums:
                res.append(path)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
            
        backtrack(nums,[])
        return res
