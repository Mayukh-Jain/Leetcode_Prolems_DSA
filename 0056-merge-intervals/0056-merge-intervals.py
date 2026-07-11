class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        res = []

        for start, end in intervals:
            if not res or res[-1][1] < start:
                res.append([start, end])
            else: 
                res[-1][1] = max(res[-1][1], end)
        
        return res