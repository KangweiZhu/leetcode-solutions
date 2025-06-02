class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
            a, aa, aab, ab, a, ab, b
        ''' 
        def isPalindrome(s):
            return s and s == s[::-1]

        m = len(s)
        result = []
        temp_result = []

        def backtrack(start):
            if start == m:
                result.append(temp_result.copy())
            
            for i in range(start, m):
                substr = s[start:i+1]
                if isPalindrome(substr):
                    temp_result.append(substr)
                    backtrack(i + 1)
                    temp_result.pop()
        
        backtrack(0)
        return result