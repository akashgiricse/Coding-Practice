def unique1(S):
    """Return true if there are no duplicates in the sequence.
        Running time complexity O(n(log n))
    """
    s = sorted(S)
    for j in range(len(s)):
        if s[j-1] == s[j]:
            return False
    return True


if __name__=='__main__':
    S = [1,2,3,4,5,6,7,8,9,9]
    print(unique1(S))
