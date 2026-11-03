class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        conteggio = {}

        for i,num in enumerate(nums):

            da_cercare = target - num

            if da_cercare in conteggio:
                return [conteggio[da_cercare],i]

            conteggio[num] = i
        
        return []