
def helloPython(input):
    output = "Hello "+input+" !"
    print(output)
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print(list(zipped))
    x2, y2 = zip(*zip(x, y))
    print(x2+y2)


helloPython("Ryan")
