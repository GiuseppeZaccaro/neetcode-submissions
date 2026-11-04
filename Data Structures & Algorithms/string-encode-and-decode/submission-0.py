class Solution:

    def encode(self, strs: List[str]) -> str:

        blocchi = []

        for parola in strs:
            blocchi.append(f"{len(parola)}#{parola}")
        
        return "".join(blocchi)


    def decode(self, s: str) -> List[str]:

        risultato = []
        i = 0
        
        while i < len(s):
        
            j = i
            while s[j] != "#":
                j += 1
                
            
            lunghezza = int(s[i:j])
            
            
            inizio_parola = j + 1
            fine_parola = inizio_parola + lunghezza
            risultato.append(s[inizio_parola:fine_parola])
            
           
            i = fine_parola
            
        return risultato
