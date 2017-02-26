def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [ O(n) - iterating through a list is O(n)   ]


    """

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [ O(n) - each lookup in a list is O(n), but 2n simplifies to O(n) because 
    the 2 makes relatively little difference as n scales]

    """

    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ O(n), lookup in a set is constant, as is appending to a list,
    so the only expensive part is creating a set in the first place]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:
        if -x in s:
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ O(n^2) lookup in a list is O(n). Since we do this in a nested
    fashion for every x and y, our runtime is quadratic]

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [ O(n^3) We still have a nested for loop that is quadratic. We also have
    to do another list lookup which is O(n) for every pair. In the best case scenario,
    result is a very short list (1 tuple), but in the worst-case it grows to the
    length of numbers/2, which is effectively O(n)]

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y and (y, x) not in result:
                result.append((x, y))
    return result
