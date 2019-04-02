def disjoint1(A,B,C):

    """Return true if there is no common element in all three lists"""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


if __name__ == '__main__':

    A = [1,2,3]
    B = [4,3,6]
    C = [7,8,3]
    print(disjoint1(A,B,C))

