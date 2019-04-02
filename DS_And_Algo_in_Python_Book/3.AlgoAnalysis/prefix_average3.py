def prefix_average3(S):
    """Return list such that for all j, A[j] equals average of S[0]...S[j]
            Complexity of the Algo: O(n)
        """
    n = len(S)
    A = [0]*n

    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total/(j+1)
    return A


if __name__ == '__main__':

    S = [1,2,3,4,5,6,7,8,9,5,4,2,2,5,8,8,5,8,5]
    print(prefix_average3(S))
