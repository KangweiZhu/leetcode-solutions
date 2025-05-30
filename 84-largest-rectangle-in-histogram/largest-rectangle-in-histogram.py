class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                previous_highest_idx = stack.pop()
                previous_highest_value = heights[previous_highest_idx]
                previous_width = i - stack[-1] -1 if stack else i
                max_area = max(max_area, previous_highest_value * previous_width)
            stack.append(i)
        return max_area