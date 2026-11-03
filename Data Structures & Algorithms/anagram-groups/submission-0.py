class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for stringa in strs:

            firma = "".join(sorted(stringa))

            if firma not in anagrams:
                anagrams[firma] = []

            anagrams[firma].append(stringa)

        return list(anagrams.values())

        

