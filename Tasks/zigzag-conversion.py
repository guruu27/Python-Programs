class Solution:
    def convert(self, s: str, rws: int) -> str:
        if rws == 1 or len(s)<=rws:
            return s
        rows = [[] for _ in range(rws)]
        idx = 0
        step = 1
        for c in s:
            rows[idx].append(c)
            if idx == 0:
                step = 1
            elif idx == rws-1:
                step = -1
            idx += step
        for r in range(rws):
            rows[r] = "".join(rows[r])
        return "".join(rows)
