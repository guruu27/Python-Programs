class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        st = []
        for p,s in sorted(pair)[::-1]:
            reach = (target - p)/s
            st.append(reach)
            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
        return len(st)
