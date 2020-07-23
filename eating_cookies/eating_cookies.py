'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # cookies can be eaten 1, 2 or 3 at a time.
    # each time a cookies are eaten, reduce the number
    # in the jar by how many were eaten at once

    # we have eaten all of the cookies
    if n == 0:
        return 1

    # return 0 the number goes negative
    # we can't eat negative cookies
    elif n < 0:
        return 0

    # add all the number of ways to eat cookies togther
    # i.e. eating cookies 1, 2 or 3 at a time
    return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
