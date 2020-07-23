'''
Input: a List of integers as well as an integer `k`
representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque


def sliding_window_max(nums, k):
    """ # len(nums) - k + 1 elements in the result array
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
    return result """

    # create a double ended que of the size of our window
    # to keep track of the arr index from our window that
    # had the greatest value
    queue = deque()

    # create a list to store the max of each window position
    result = []

    # iterate through the first window of elements in the array
    for i in range(k):
        # we don't need to keep elements that are smaller than the current max
        while queue and nums[i] >= nums[queue[-1]]:
            queue.pop()

        # add the new element to the queue
        queue.append(i)

    # move the window through the rest of the array
    for i in range(k, len(nums)):

        # the max value of the window pass is at the front of the queue
        # we need to store this in the results list
        result.append(nums[queue[0]])

        # remove elements from the queue that are outside the current window
        while queue and queue[0] <= i - k:
            # remove from the front of the queue
            queue.popleft()

        # repeat the process of finding the max value in the window area
        # we don't need to keep elements that are smaller than the current max
        while queue and nums[i] >= nums[queue[-1]]:
            queue.pop()

        # add the new element to the queue
        queue.append(i)

    # store the max value from the last window
    result.append(nums[queue[0]])

    # return the result list
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
