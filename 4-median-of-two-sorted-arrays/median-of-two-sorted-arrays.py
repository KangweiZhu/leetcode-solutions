class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        merged_list = []
        
        m_idx = 0
        n_idx = 0
        while m_idx < m and n_idx < n:
            m_val = nums1[m_idx]
            n_val = nums2[n_idx]
            if m_val >= n_val:
                merged_list.append(n_val)
                n_idx += 1
            else:
                merged_list.append(m_val)
                m_idx += 1
        
        while m_idx < m:
            merged_list.append(nums1[m_idx])
            m_idx += 1

        while n_idx < n:
            merged_list.append(nums2[n_idx])
            n_idx += 1
        
        result_idx = (m + n) >> 1
        return merged_list[result_idx] if (m + n) % 2 != 0 else (merged_list[result_idx] + merged_list[result_idx - 1]) / 2