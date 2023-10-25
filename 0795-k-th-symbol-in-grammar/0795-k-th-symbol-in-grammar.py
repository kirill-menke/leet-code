class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        row_length = 2**(n - 1)

        if k > row_length / 2:
            return 1 - self.kthGrammar(n, k - row_length / 2)
        else:
            return self.kthGrammar(n - 1, k)
        