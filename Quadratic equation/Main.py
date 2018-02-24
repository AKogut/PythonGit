
print("ax^2 + bx + c = 0")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = (b**2) - (4 * a * c)
if D > 0:
    import math
    x1 = (- b + math.sqrt(D)) / (2 * a)
    x2 = (- b - math.sqrt(D)) / (2 * a)
    print("x1 = %.2f" % x1)
    print("x2 = %.2f" % x2)
elif D == 0:
    x = (- b) / (2 * a)
    print("x = %.2f" % x)
else:
    print("Error %.2f < 0" % D)





