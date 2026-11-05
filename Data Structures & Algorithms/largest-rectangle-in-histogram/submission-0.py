class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = [] 

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                prev_index, prev_height = stack.pop()
                larghezza = i - prev_index
                max_area = max(max_area, prev_height * larghezza)
                start = prev_index
            
            stack.append([start, h])

        n = len(heights)
        for start, h in stack:
            larghezza = n - start
            max_area = max(max_area, h * larghezza)

        return max_area

