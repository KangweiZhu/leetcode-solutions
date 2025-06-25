class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keymap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        result = []
        temp_result = []
        def backtrack(start):
            if start == len(digits):
                result.append(''.join(temp_result))
                return 
            combo = keymap[digits[start]]
            for key in combo:
                temp_result.append(key)
                backtrack(start + 1)
                temp_result.pop()
        backtrack(0)
        return result