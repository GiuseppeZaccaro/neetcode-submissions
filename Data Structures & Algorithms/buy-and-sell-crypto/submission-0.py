class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0  
        profitto_massimo = 0
    
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                profitto_corrente = prices[right] - prices[left]
                profitto_massimo = max(profitto_massimo, profitto_corrente)
            else:
                left = right
                
        return profitto_massimo





