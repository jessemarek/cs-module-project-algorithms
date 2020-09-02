'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    """ # create a new array to hold the product values
    result = [0] * len(arr)

    # for each index, look at every other number in the list.
    for i in range(len(arr)):
        product = 1

        # multiply all the numbers in the array together
        for j in range(len(arr)):
            product *= arr[j]

        # replace the current index with the product
        # divided by the current index
        result[i] = product // arr[i]

    return result """

    # create a new array to hold the product values
    result = [0] * len(arr)

    # for each index we need to get the product of all
    # the elements below and above it

    for i in range(len(arr)):
        # set pointers to the current index, left and right
        left = right = i
        # store the product to the left and right of the current index
        prod_left = prod_right = 1

        # while we have elements to the left of the current index
        # multiply them together
        while left > 0:
            left -= 1
            prod_left *= arr[left]

        # while we have elements to the right of the current index
        # multiply them together
        while right <= len(arr)-2:
            right += 1
            prod_right *= arr[right]

        # the result is the product of the left and right products
        result[i] = prod_left * prod_right

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #       9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
