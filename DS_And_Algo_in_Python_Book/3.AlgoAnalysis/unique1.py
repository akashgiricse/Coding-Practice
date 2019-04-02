def unique1(S):
    """Return true if there are no duplicates in the sequence.
        Running time complexity O(n2)
    """
    for j in range(len(S)):
        for i in range(j+1, len(S)):
            if S[j] == S[i]:
                return False
    return True


if __name__=='__main__':
    S = [1,2,3,4,5,6,7,8,9]
    print(unique1(S))
