def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(dp)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(X[i - 1],Y[j - 1])
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    # Backtrack to find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
            print(lcs)
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()

    return dp[m][n], ''.join(lcs)

# Example usage
sequence_A = "ABCDGH"
sequence_B = "AEDFHR"
length, lcs = longest_common_subsequence(sequence_A, sequence_B)
print(f"Length of LCS: {length}")
print(f"LCS: {lcs}")
