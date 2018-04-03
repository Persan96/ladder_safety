import sys, math

for i in sys.stdin:
    arguments = i.split()
    length = float(arguments[0])
    angle = math.cos(math.radians(90-float(arguments[1])))
    result = math.ceil(length/angle)
    print(result)