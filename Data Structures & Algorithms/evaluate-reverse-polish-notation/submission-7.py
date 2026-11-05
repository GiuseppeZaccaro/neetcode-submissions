import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        mappa = {'+':operator.add, '-':operator.sub,'*':operator.mul,'/': lambda a, b: int(a / b)}

        stack = []

        for char in tokens:

            if char in mappa:
                num2 = stack.pop()
                num1 = stack.pop()

                risultato = mappa[char](num1, num2)

                stack.append(risultato)
            else:
                stack.append(int(char))

        return stack[0] 
