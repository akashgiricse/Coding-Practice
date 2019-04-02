def binary_search(data, target, low, high):
    """Binary search. Complexity (log n)"""

    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:

            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


if __name__=='__main__':

    print(binary_search([2,4,5,7,8,9,18,43,67], 18,0, 8))