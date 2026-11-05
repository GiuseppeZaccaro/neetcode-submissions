class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        mappa = {')': '(', '}': '{', ']': '['}
        stack = []

        for carattere in s:
            if carattere in mappa:
                elemento_cima = stack.pop() if stack else '#'
                if elemento_cima != mappa[carattere]:
                    return False
            else:
                stack.append(carattere)

        return not stack


