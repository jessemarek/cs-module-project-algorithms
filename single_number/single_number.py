'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    """ # look at each number in the list
    for i in range(len(arr)):
        # if the number exists more than once it is not unique
        if arr[i] not in arr[:i] and arr[i] not in arr[i+1:]:
            return arr[i] """

    # keep track of the values in the array
    # starting with the first value in the list
    result = arr[0]

    # iterate over the array starting at the second number
    for i in range(1, len(arr)):
        # use the xOR bitwise operator to 'cancel out' duplicate values
        result ^= arr[i]

    # result should be the only value in the list that is not duplicated
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
