class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+ nums2
        nums.sort()
        if len(nums)%2!=0:
            return nums[len(nums)//2]
        mid = len(nums)//2
        print(nums[mid])
        print(nums[mid-1])
        median = nums[mid]+nums[mid-1]
        return median/2
