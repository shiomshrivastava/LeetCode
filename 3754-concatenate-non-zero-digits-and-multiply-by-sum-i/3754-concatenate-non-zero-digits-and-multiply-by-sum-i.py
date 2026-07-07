class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ''.join(ch for ch in str(n) if ch != '0')
        return 0 if not s else int(s) * sum(int(ch) for ch in s)