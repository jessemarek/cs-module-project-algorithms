'''
Input: a List of integers as well as an integer `k`
representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # len(nums) - k + 1 elements in the result array

    # window is smaller than the list size
    # window moves over 1 element at a time
    result = []
    for i in range(len(nums) - k + 1):
        # set max value to first element in the sliding window
        max_value = nums[i]
        # iterate over elements in the sliding window
        for j in range(i, i + k):
            # if the current element value is greater than the max
            # replace the max value with the current index value
            if nums[j] > max_value:
                max_value = nums[j]
        # aadd the max value from that window to the results list
        result.append(max_value)
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
