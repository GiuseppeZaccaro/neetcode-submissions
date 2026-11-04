class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        risultato = [1] * n 
        
        prefisso = 1
        for i in range(n):
            risultato[i] = prefisso
            prefisso *= nums[i]
            
        suffisso = 1
        for i in range(n - 1, -1, -1):
            risultato[i] *= suffisso
            suffisso *= nums[i]
            
        return risultato
