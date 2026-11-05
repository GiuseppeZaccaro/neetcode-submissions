class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        risultato = [0] * n
        
        stack = []

        for i in range(n):
            temperatura_oggi = temperatures[i]

            while stack and temperatura_oggi > temperatures[stack[-1]]:
                indice_passato = stack.pop()
                risultato[indice_passato] = i - indice_passato

            stack.append(i)

        return risultato    
            

                
        


            
