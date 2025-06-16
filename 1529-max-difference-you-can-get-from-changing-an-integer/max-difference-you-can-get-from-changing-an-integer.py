class Solution:
    def maxDiff(self, num: int) -> int:
        left = 0
        stringnified_num = str(num)
        m = len(stringnified_num)
        right = m - 1
        max_num = num
        ptr = 0
        while ptr <= right:
            if stringnified_num[ptr] != '9':
                stringnified_num = stringnified_num.replace(stringnified_num[ptr], '9')
                max_num = max(max_num, int(stringnified_num))
                break
            ptr += 1
        
        ptr = left
        min_num = num
        stringnified_num = str(num)
        while ptr <= right:
            if stringnified_num[ptr] != '0' and stringnified_num[ptr] != '1':
                if ptr == 0:
                    stringnified_num = stringnified_num.replace(stringnified_num[ptr], '1')
                else:
                    stringnified_num = stringnified_num.replace(stringnified_num[ptr], '0')
                min_num = min(min_num, int(stringnified_num))
                break
            ptr += 1
        return max_num - min_num
        
        