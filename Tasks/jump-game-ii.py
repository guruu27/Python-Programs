#jump-game-ii


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        curr_end,curr_far = 0,0
        for i in range(len(nums)-1):
            curr_far = max(curr_far,i+nums[i])
            if i==curr_end:
                ans+=1
                curr_end = curr_far

        return ans
