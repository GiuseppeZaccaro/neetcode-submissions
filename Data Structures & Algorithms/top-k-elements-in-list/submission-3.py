class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        conteggio = {}
        result = set()
        for num in nums:
            
            conteggio[num] = conteggio.get(num,0) + 1

        numeri_ordinati = sorted(conteggio.keys(), key=lambda x: conteggio[x], reverse=True)

        return numeri_ordinati[:k]
            

