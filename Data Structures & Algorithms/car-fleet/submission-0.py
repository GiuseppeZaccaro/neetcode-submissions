class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        macchine = list(zip(position, speed))
        
        macchine.sort(key=lambda x: x[0], reverse=True)
        
        stack = [] 
        
        for pos, spd in macchine:

            tempo = (target - pos) / spd
            stack.append(tempo)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)



