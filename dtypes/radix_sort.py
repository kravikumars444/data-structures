def radsort(unslist):
    """Returns a sorted list. Accepts only a list containing positive
    integers."""
    # find max for iterative solution
    maxval = max(unslist)
    ntimes = len(str(maxval))

    slist = unslist[:]

    for n in range(ntimes):
        # Making radix bins
        bins = [[] for _ in range(10)]

        # Place each list item in appropriate bin
        for i, item in enumerate(slist):
            inspecting = slist[i]
            digval = _get_nth_digit(inspecting, n)
            bins[digval].append(inspecting)

        slist = []
        # Flatten bins to list
        for bin in bins:
            slist.extend(bin)

    return slist


def _get_nth_digit(num, n):
    """For a positive integer, get the value at the nth digit;
    indexing starts at 0"""

    return ((num % (10 ** (n + 1))) - (num % (10 ** n))) // 10 ** n


if __name__ == "__main__":
    """Test time performance for best and worst cases"""
    import time

    size = 1000

    # Best case: when all numbers in the list have the same number of digits.
    good_list = range(size + 1)
    start = time.time()
    for i in range(1000):
        radsort(good_list)
    stop = time.time()
    best_time = (stop - start)

    # Worst case: When there is one very large outlier.
    bad_list = [1 for _ in range(size)] + [10**10]
    start = time.time()
    for i in range(1000):
        radsort(bad_list)
    stop = time.time()
    worst_time = (stop - start)

    print "Best case is {} times better than worst for n=1000\n".format(
        worst_time/best_time)
    print "Best case:  {0:.{1}f} ms\nWorst case: {2:.{3}f} ms".format(
        best_time, 5, worst_time, 5)
