def pascal_triangle(n):

    if n <= 0:
        return[]

    triangle_index = [[1]]
    while len(triangle_index) != n:

        adjacent = triangle_index[-1]
        actual = [1]

        for x in range(len(adjacent) - 1):
            actual.append(adjacent[x] + adjacent[x + 1])
        actual.append(1)
        triangle_index.append(actual)

    return triangle_index
