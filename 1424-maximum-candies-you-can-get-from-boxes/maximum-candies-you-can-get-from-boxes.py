class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        max_candy_num = 0
        package = deque(initialBoxes)

        def package_contain_openable(pacakge):
            '''
                Check if the there are still boxes that are able to be unboxed.
            '''
            for idx in package:
                if status[idx] == 1 or keys[idx] == 1:
                    return True
            return False

        while package:
            if not package_contain_openable(package):
                break

            curr_level_len = len(package)
            
            for _ in range(curr_level_len):
                idx = package.popleft()
                if status[idx] == 1:
                    max_candy_num += candies[idx]
                    package.extend(containedBoxes[idx])
                    for curr_keys in keys[idx]:
                        status[curr_keys] = 1
                else:
                    package.append(idx)
        
        return max_candy_num