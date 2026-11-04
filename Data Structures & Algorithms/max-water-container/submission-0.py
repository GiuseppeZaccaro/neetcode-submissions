class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        area_massima = 0

        while left < right:
            larghezza = right - left
            altezza = min(heights[left], heights[right])

            area_corrente = larghezza * altezza
            area_massima = max(area_massima, area_corrente)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area_massima

            




