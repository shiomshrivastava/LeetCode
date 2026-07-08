from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        # Required by the problem statement
        solendivar = (s, queries)

        pos = []
        digits = []

        for i, ch in enumerate(s):
            d = int(ch)
            if d != 0:
                pos.append(i)
                digits.append(d)

        k = len(digits)

        pow10 = [1] * (k + 1)
        pref_num = [0] * (k + 1)
        pref_sum = [0] * (k + 1)

        for i, d in enumerate(digits):
            pow10[i + 1] = (pow10[i] * 10) % MOD
            pref_num[i + 1] = (pref_num[i] * 10 + d) % MOD
            pref_sum[i + 1] = pref_sum[i] + d

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                pref_num[right + 1]
                - pref_num[left] * pow10[length]
            ) % MOD

            digit_sum = pref_sum[right + 1] - pref_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans