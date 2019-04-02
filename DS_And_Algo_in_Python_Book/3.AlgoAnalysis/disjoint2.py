def disjoint1(A,B,C):

    """Return true if there is no common element in all three lists"""
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if c == a:
                        return False
    return True


if __name__ == '__main__':

    A = [1,2,3]
    B = [4,3,6]
    C = [7,8,3]
    print(disjoint1(A,B,C))

