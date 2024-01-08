#!/usr/bin/python3
""" This is a simple method to solve a pascal traingle problem. """

def pascal_triangle(n):
    """if the given n value is less or equals 1
    the function returns empty list."""
    if n <= 0:
        return []
    triangle = []
    for x in range(1, n+1):
        """This loop keeps track of the size of the triangle."""
        inner = []
        for y in range(1, x+1):
            """This loop is where the real magic happens."""
            if(y == 1 or y == x):
                inner.append(1)
            else:
                ## look for the previous elements.
                temp = triangle[x-2]
                value = temp[y-2] + temp[y-1]
                inner.append(value)
        triangle.append(inner)

    return triangle
