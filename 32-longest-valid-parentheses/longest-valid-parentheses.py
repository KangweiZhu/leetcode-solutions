class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        lvp = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    lvp = max(lvp, i - stack[-1])
            else:
                raise ValueError(f'Invalid character at index {i}: {ch}!')
        
        return lvp