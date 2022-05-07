def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    s1 = set(nums)
    l1 = [n for n in s1]
    l2 = [nums.count(num) for num in s1]
    return l1[l2.index(max(l2))]