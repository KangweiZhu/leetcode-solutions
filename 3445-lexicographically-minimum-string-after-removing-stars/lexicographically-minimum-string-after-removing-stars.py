import heapq
from collections import defaultdict

class Solution:
    def clearStars(self, s: str) -> str:
        stack = []
        char_indices = defaultdict(list)  # 记录每个字符在 stack 中的索引
        min_heap = []

        for ch in s:
            if ch != '*':
                idx = len(stack)
                stack.append(ch)
                char_indices[ch].append(idx)
                heapq.heappush(min_heap, ch)
            else:
                while min_heap:
                    min_char = heapq.heappop(min_heap)
                    if char_indices[min_char]:  # 该字符还有有效位置
                        idx = char_indices[min_char].pop()
                        stack[idx] = ''  # 标记为已删除
                        break  # 只删一次
        return ''.join(c for c in stack if c)
