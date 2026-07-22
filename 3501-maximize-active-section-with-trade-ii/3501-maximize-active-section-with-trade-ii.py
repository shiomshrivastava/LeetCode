from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        starts, ends, vals = [], [], []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            starts.append(i)
            ends.append(j - 1)
            vals.append(1 if s[i] == '1' else 0)
            i = j
        m = len(starts)
        run_len = [ends[k] - starts[k] + 1 for k in range(m)]
        total_ones = s.count('1')

        # position -> run index
        pos_run = [0] * n
        for k in range(m):
            pos_run[starts[k]:ends[k] + 1] = [k] * run_len[k]

        NEG = -1
        G = [NEG] * m
        for i in range(1, m - 1):
            if vals[i] == 1:
                G[i] = run_len[i - 1] + run_len[i + 1]

        # sparse table for range-max on G
        K = 1
        while (1 << K) <= m:
            K += 1
        sp = [G]
        for k in range(1, K):
            half = 1 << (k - 1)
            length = 1 << k
            prev = sp[-1]
            cur = [NEG] * m
            for idx in range(m - length + 1):
                x, y = prev[idx], prev[idx + half]
                cur[idx] = x if x > y else y
            sp.append(cur)

        log_table = [0] * (m + 1)
        for i in range(2, m + 1):
            log_table[i] = log_table[i // 2] + 1

        def range_max(l, r):
            if l > r:
                return NEG
            k = log_table[r - l + 1]
            v1, v2 = sp[k][l], sp[k][r - (1 << k) + 1]
            return v1 if v1 > v2 else v2

        ans = []
        for l, r in queries:
            a = pos_run[l]
            b = pos_run[r]
            M = 0
            if b > a + 1:
                if b == a + 2:
                    if vals[a + 1] == 1:
                        L = ends[a] - l + 1
                        R = r - starts[b] + 1
                        M = L + R
                else:
                    cand = 0
                    if vals[a + 1] == 1:
                        L = ends[a] - l + 1
                        R = run_len[a + 2]
                        if L + R > cand:
                            cand = L + R
                    if vals[b - 1] == 1:
                        L = run_len[b - 2]
                        R = r - starts[b] + 1
                        if L + R > cand:
                            cand = L + R
                    if a + 2 <= b - 2:
                        rm = range_max(a + 2, b - 2)
                        if rm > cand:
                            cand = rm
                    M = cand
            ans.append(total_ones + M)
        return ans