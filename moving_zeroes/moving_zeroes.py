'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):

    # loop through each item in the list
    for i in range(len(arr) - 1):
        # check the next value and compare.
        # If a 0 is on the left swap spots
        for j in range(len(arr) - i - 1):
            if arr[j] == 0 and arr[j+1] != 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
