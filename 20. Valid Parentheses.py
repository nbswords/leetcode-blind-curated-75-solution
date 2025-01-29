class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # key of dict is right and value is left
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            # if c is brackets
            if c in pairs:
                # stack is empty or Top is not equal to left of c
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                # c is left and in the pairs
                stack.append(c)
        return not stack
