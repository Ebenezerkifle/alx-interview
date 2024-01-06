#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for x in range(1, n+1):
        inner = []
        for y in range(1, x+1):
            inner.append(y)
        triangle.append(inner)
    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))