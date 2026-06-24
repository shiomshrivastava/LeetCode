class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1
        size = 2 * m

        def mat_mul(A, B):
            C = [[0] * size for _ in range(size)]

            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue

                    aik = A[i][k]

                    for j in range(size):
                        if B[k][j]:
                            C[i][j] = (
                                C[i][j] +
                                aik * B[k][j]
                            ) % MOD

            return C

        def mat_pow(M, p):
            R = [[0] * size for _ in range(size)]

            for i in range(size):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)

                M = mat_mul(M, M)
                p >>= 1

            return R

        T = [[0] * size for _ in range(size)]

        for x in range(m):

            for y in range(x + 1, m):
                T[y][x + m] = 1

            for y in range(x):
                T[y + m][x] = 1

        P = mat_pow(T, n - 1)

        init = [1] * size

        ans = 0

        for i in range(size):
            cur = 0

            for j in range(size):
                cur = (cur + P[i][j] * init[j]) % MOD

            ans = (ans + cur) % MOD

        return ans