class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        output = set(nums)
        lunghezza_massima = 0

        for num in output:

            if num-1 not in output:
                corrente = num
                lunghezza_corrente = 1

                while (corrente + 1) in output:
                    corrente += 1
                    lunghezza_corrente += 1
                
                lunghezza_massima = max(lunghezza_massima, lunghezza_corrente)

        return lunghezza_massima


        
            
            
            



            