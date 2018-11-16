"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    # modulo nrows % 2 and ncols % 2
    # if modulo is not zero, calculate middle
    # if modulo is zero, take two middle values

    # using values obtained, determine start cell as cell with highest initial value

    # start loop
    # if cell value is zero, stop

    # if not, increase carrots eaten by value
    # set cell value to zero

    # add WNES values to list, loop through to find highest, and index of highest
    # index 0 -> go W... index 3 -> go S

    # repeat until cell initial cell value is zero

    r = []
    c = []
    if nrows % 2 == 0:
        r.append(int(nrows/2 - 1))
        r.append(int(nrows/2))
    else:
        r.append(int(nrows/2))

    if ncols % 2 == 0:
        c.append(int(ncols/2 - 1))
        c.append(int(ncols/2))
    else:
        c.append(int(ncols/2))

    value = garden[r[0]][c[0]]
    index = [r[0], c[0]]

    for i in range(len(r)):
        for j in range(len(c)):
            new_value = garden[i+r[0]][j+c[0]]
            if new_value > value:
                value = new_value
                index = [i + r[0], j + c[0]]

    carrots = 0
    while value != 0:
        carrots += value
        garden[index[0]][index[1]] = 0
        value = 0

        # check W
        if index[0] >= 0 and index[0] < nrows and index[1]-1 >= 0 and index[1]-1 < ncols:
        # try:
            if garden[index[0]][index[1]-1] > value:
                value = garden[index[0]][index[1]-1]
                new_index = [index[0],index[1]-1]   
        # except:
        #     continue

        # check n
        if index[0]-1 >= 0 and index[0]-1 < nrows and index[1] >= 0 and index[1] < ncols:
        # try:
            if garden[index[0]-1][index[1]] > value:
                value = garden[index[0]-1][index[1]]
                new_index = [index[0]-1,index[1]]
        # except:
        #     continue

        # check e
        if index[0] >= 0 and index[0] < nrows and index[1]+1 >= 0 and index[1]+1 < ncols:
            # print(index[0],(index[1]+1))
        # try:
            if garden[index[0]][index[1]+1] > value:
                value = garden[index[0]][index[1]+1]
                new_index = [index[0],index[1]+1]
        # except:
        #     continue

        # check s
        if index[0]+1 >= 0 and index[0]+1 < nrows and index[1] >= 0 and index[1] < ncols:
        # try:
            if garden[index[0]+1][index[1]] > value:
                value = garden[index[0]+1][index[1]]
                new_index = [index[0]+1,index[1]]
        # except:
        #     continue

        index=new_index


    return carrots     


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
