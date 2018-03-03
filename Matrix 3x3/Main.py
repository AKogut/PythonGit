print("Enter matrix 3x3")
number = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Enter first line
number[0][0] = int(input("a11 = "))
number[0][1] = int(input("a12 = "))
number[0][2] = int(input("a13 = "))

# Enter second line
number[1][0] = int(input("a21 = "))
number[1][1] = int(input("a22 = "))
number[1][2] = int(input("a23 = "))

# Enter third line
number[2][0] = int(input("a31 = "))
number[2][1] = int(input("a32 = "))
number[2][2] = int(input("a33 = "))

print("Matrix")
# Output first line
print(number[0][0], number[0][1], number[0][2])
# Output second line
print(number[1][0], number[1][1], number[1][2])
# Output third line
print(number[2][0], number[2][1], number[2][2])

# Search determinant
determinant1 = (number[0][0] * number[1][1] * number[2][2]) + (number[1][0] * number[2][1] * number[0][2])
+ (number[0][1] * number[1][2] * number[2][0])

determinant2 = (number[0][2] * number[1][1] * number[2][0]) + (number[2][1] * number[1][2] * number[0][0])
+ (number[1][0] * number[0][1] * number[2][2])

# Output determinant
determinant = float(determinant1 - determinant2)
print(determinant1)
print(determinant2)
print("determinant = %.2f" % determinant)

