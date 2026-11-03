class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        conteggio = {}

        if (len(s) != len(t)):
            return False
        
        for char in s:
            conteggio[char] = conteggio.get(char,0) + 1
        
        for char in t:
            if char not in conteggio or conteggio[char] == 0:
                return False
            conteggio[char] -= 1

        return True