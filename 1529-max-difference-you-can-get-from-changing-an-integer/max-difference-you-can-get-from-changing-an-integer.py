class Solution:
    def maxDiff(self, num: int) -> int:
        stringnified_num = str(num)
        m = len(stringnified_num)
        right = m - 1
        
        # 构造最大值
        ptr = 0
        max_num = num
        while ptr <= right:
            if stringnified_num[ptr] != '9':
                max_version = stringnified_num.replace(stringnified_num[ptr], '9')
                max_num = int(max_version)
                break
            ptr += 1

        # 构造最小值
        ptr = 0
        min_num = num
        stringnified_num = str(num)
        while ptr <= right:
            ch = stringnified_num[ptr]
            if ch != '0' and ch != '1':
                if ptr == 0:
                    # 首位不能替换为 0，只能替换为 1
                    min_version = stringnified_num.replace(ch, '1')
                else:
                    min_version = stringnified_num.replace(ch, '0')
                min_num = int(min_version)
                break
            ptr += 1

        return max_num - min_num
