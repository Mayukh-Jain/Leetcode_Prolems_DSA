class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                he=heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area=max(max_area,he*w)
            stack.append(i)
        return max_area