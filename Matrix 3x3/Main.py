print("Enter matrix 3x3")
number = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Enter first line
number[0] = int(input("a11 = "))
number[1] = int(input("a12 = "))
number[2] = int(input("a13 = "))

# Enter second line
number[3] = int(input("a21 = "))
number[4] = int(input("a22 = "))
number[5] = int(input("a23 = "))

# Enter third line
number[6] = int(input("a31 = "))
number[7] = int(input("a32 = "))
number[8] = int(input("a33 = "))

print("Matrix")
# Output first line
print(number[0], number[1], number[2])
# Output second line
print(number[3], number[4], number[5])
# Output third line
print(number[6], number[7], number[8])

# Search determinant
det1 = (number[0] * number[4] * number[8]) + (number[3] * number[7] * number[2]) + (number[1] * number[5] * number[6])

det2 = (number[6] * number[4] * number[2]) + (number[7] * number[5] * number[0]) + (number[3] * number[1] * number[8])

# Output determinant
determinant = float(det1 - det2)
print("determinant = %.2f" % determinant)

