class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        risultato = []

        for i in range(n-2):

            if nums[i]>0:
                break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i +1
            right = len(nums) - 1

            while left < right:
                
                somma = nums[i] + nums[left] + nums[right]
                
                if somma < 0:
                        left += 1
                elif somma > 0:
                    right -= 1
                else:
                    risultato.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                        
                    while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return risultato



        