class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        start=0
        prev_gas=0
        curr_gas=0
        for i in range(n):
            curr_gas+=(gas[i]-cost[i])
            if curr_gas<0:
                start=i+1
                prev_gas+=curr_gas
                curr_gas=0
        return start if curr_gas+prev_gas>=0 else -1