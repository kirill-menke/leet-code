class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                prev_idx = stack[-1]
                cur_width = i - prev_idx - 1
                max_area = max(max_area, cur_height * cur_width)
            stack.append(i)
        
        while stack[-1] != -1:
            cur_height = heights[stack.pop()]
            prev_idx = stack[-1]
            cur_width = len(heights) - prev_idx - 1
            max_area = max(max_area, cur_height * cur_width)
        
        return max_area