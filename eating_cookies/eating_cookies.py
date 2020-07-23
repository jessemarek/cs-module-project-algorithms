'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache):
    # cookies can be eaten 1, 2 or 3 at a time.
    # each time a cookies are eaten, reduce the number
    # in the jar by how many were eaten at once
    """     # we have eaten all of the cookies
    if n == 0:
        return 1

    # return 0 the number goes negative
    # we can't eat negative cookies
    elif n < 0:
        return 0

    # add all the number of ways to eat cookies togther
    # i.e. eating cookies 1, 2 or 3 at a time
    return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1) """

    # we have eaten all of the cookies
    if n == 0:
        return 1

    # return 0 the number goes negative
    # we can't eat negative cookies
    elif n < 0:
        return 0

    # check if the answer exists in our cache
    # before making a further recusrive call
    elif cache[n] > 0:
        return cache[n]

    # add all the number of ways to eat cookies togther
    # i.e. eating cookies 1, 2 or 3 at a time
    else:
        cache[n] = eating_cookies(
            n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)

        return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    cache = {i: 0 for i in range(num_cookies + 1)}

    print(
        f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to eat {num_cookies} cookies")
