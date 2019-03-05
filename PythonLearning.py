import xmath
import xmath as math


def helloPython(input):
    output = "Hello "+input+" !"
    print(output)
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print(list(zipped))
    x2, y2 = zip(*zip(x, y))
    print(x2+y2)
    # --------
    print(xmath.pi)
    max = xmath.max(10, 5)
    min = xmath.min(4, 10)
    sum = xmath.sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(max)
    print(min)
    print(sum)
    print(math.e)


helloPython("Ryan")
