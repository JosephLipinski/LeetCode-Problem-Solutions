class Median:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import numpy as np
        m = nums1
        n = nums2
        len_m = len(m)
        len_n = len(n)
        total_len = len_m + len_n
        if total_len == 2:
            if m != [] and n != []:
                return (m[0] + n[0]) / 2
            elif m != []:
                return (m[0] + m[1]) / 2
            else:
                return (n[0] + n[1]) / 2
        elif total_len == 1:
            return m[0] if m != [] else n[0]
        else:
            try:
                m_0 = m[0]
            except IndexError:
                m_0 = np.NINF
            try:
                n_0 = n[0]
            except IndexError:
                n_0 = np.NINF
            try:
                m_i = m[-1]
            except:
                m_i = np.inf
            try:
                n_j = n[-1]
            except:
                n_j = np.inf
            
            if m_0 >= n_0:
                if n_0 != np.NINF:
                    n = n[1:]
                else:
                    m = m[1:]
            else:
                if m_0 != np.NINF:
                    m = m[1:]
                else:
                    n = n[1:]
            
            if m_i >= n_j:
                if m_i != np.inf:
                    m = m[:-1]
                else:
                    n = n[:-1]
            else:
                if n_j != np.inf:
                    n = n[:-1]
                else:
                    m = m[:-1]
                
            return self.findMedianSortedArrays(m, n)
