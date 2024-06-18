class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        res,best,j = 0,0,0
        jobs = sorted(zip(difficulty,profit))
        print(jobs)
        for w in worker:
            while j<len(jobs) and jobs[j][0]<=w:
                best = max(best,jobs[j][1])
                j+=1
            res+=best
        return res
