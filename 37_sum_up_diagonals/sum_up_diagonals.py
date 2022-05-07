def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    k = len(matrix[0])
    product1 = 0
    product2 = 0
    for x in range(0, k):   
        product1 = product1 + matrix[x][x]
    for y in range(0, k):
        product2 = product2 + matrix[y][(-y-1)]
    return product1 + product2

