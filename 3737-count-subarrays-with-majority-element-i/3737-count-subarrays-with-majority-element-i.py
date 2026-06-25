from typing import List
from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Prefix sum
        pref = [0]
        curr = 0
        for x in nums:
            curr += 1 if x == target else -1
            pref.append(curr)

        # Coordinate compression
        vals = sorted(set(pref))

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def update(self, idx, val):
                idx += 1
                while idx <= self.n:
                    self.bit[idx] += val
                    idx += idx & -idx

            def query(self, idx):
                idx += 1
                s = 0
                while idx > 0:
                    s += self.bit[idx]
                    idx -= idx & -idx
                return s

        fw = Fenwick(len(vals))
        ans = 0

        for p in pref:
            idx = bisect_left(vals, p)

            # count previous prefix sums < current prefix sum
            if idx > 0:
                ans += fw.query(idx - 1)

            fw.update(idx, 1)

        return ans