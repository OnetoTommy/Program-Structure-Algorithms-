class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)

        # dp[i][j] means min edits to convert word1[0:i] to word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: converting from/to empty strings
        for i in range(m + 1):
            dp[i][0] = i  # delete all i characters
        for j in range(n + 1):
            dp[0][j] = j  # insert all j characters

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    diff = 0
                else:
                    diff = 1

                dp[i][j] = min(
                    dp[i - 1][j - 1] + diff,  # substitute
                    dp[i - 1][j] + 1,         # delete
                    dp[i][j - 1] + 1          # insert
                )

        return dp[m][n]
