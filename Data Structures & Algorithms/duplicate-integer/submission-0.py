class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visti = set()

        for num in nums:
            if num in visti:
                return True
            else:
                visti.add(num)
        
        return False

            