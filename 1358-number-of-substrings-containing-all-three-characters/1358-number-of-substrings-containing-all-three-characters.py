class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        ans = 0
        n = len(s)

        for right in range(n):
            count[s[right]] += 1

            # Jab tak window valid hai
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - right
                count[s[left]] -= 1
                left += 1

        return ans