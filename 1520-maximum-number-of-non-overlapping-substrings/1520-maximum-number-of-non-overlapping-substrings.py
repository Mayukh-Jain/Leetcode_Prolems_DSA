class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []
        for ch, start in first.items():
            end = last[ch]
            is_valid = True
            
            i = start
            while i <= end:
                c = s[i]
                if first[c] < start:
                    is_valid = False
                    break
                end = max(end, last[c])
                i += 1
                
            if is_valid:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        res = []
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                res.append(s[start : end + 1])
                last_end = end

        return res