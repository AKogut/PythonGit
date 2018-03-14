print("Private bank")
print("Alfa Bank")
print("Aval Bank")
chooseBank = input("Choose bank: ")
if chooseBank == "private bank":
    # deposit 10%
    money = int(input("Enter sum of money: "))
    money = money + (money * 0.1)
    print("After 1 years you have %.2f" % money)
    print("Private Bank")
elif chooseBank == "alfa bank":
    # deposit 8%
    money = int(input("Enter sum of money: "))
    money = money + (money * 0.08)
    print("After 1 years you have %.2f" % money)
    print("Alfa Bank")
elif chooseBank == "aval bank":
    # deposit 12%
    money = int(input("Enter sum of money: "))
    money = money + (money * 0.12)
    print("After 1 years you have %.2f" % money)
    print("Aval Bank")
else:
    print("Error")
