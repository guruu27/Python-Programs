class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import defaultdict 
        count_map = defaultdict(int)
        remaining = []
        res = []

        for num in arr2:
            count_map[num] = 0
        
        for num in arr1:
            if num in count_map:
                count_map[num]+=1
            else:
                remaining.append(num)
        
        remaining.sort()

        for num in arr2:
            res.extend([num]*count_map[num])
        
        res.extend(remaining)
        
        return res
