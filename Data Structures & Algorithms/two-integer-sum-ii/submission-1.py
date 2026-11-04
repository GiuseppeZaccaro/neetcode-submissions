class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            somma_corrente = numbers[left] + numbers[right]
            
            if somma_corrente == target:
                return [left + 1, right + 1]
            elif somma_corrente < target:
                left += 1
            else:
                right -= 1
                
        return []

    
                
               
