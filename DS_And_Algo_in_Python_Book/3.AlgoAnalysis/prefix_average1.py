def prefix_average1(S):

    """Return list such that for all j, A[j] equals average of S[0]...S[j]
        Complexity of the Algo: O(n2)
    """

    n = len(S)
    A = [0]*n  # a new list of n zeros
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total/(j+1)
    return A


if __name__ == '__main__':
    S = [1,2,3,4,5,6,7,8,9,5,8,4,7,5,8,4,7,5,6,2,4,8,5,8]
    print(prefix_average1(S))

