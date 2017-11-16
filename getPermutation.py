class Solution:
    """
    @param: n: n
    @param: k: the k th permutation
    @return: return the k-th permutation
    """

    def getPermutation(self, n, k):
        # write your code here
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[-1] * i)

        elegible = range(1, n + 1)
        per = []
        for i in range(n):
            digit = (k - 1) / fac[n - i - 1]
            per.append(elegible[digit])
            elegible.remove(elegible[digit])
            k = (k - 1) % fac[n - i - 1] + 1
        return "".join([str(x) for x in per])