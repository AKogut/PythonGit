class Wallet:
    balance = 130
    refill = 0
    game = 0
    entertainment = 0
    meal = 0
    other = 0
    ctg = [game, entertainment, meal, other]


wallet = Wallet()
while True:
    print("<----------------------->")
    print("refill")
    print("withdraw")
    print("report")
    print("balance")
    print("exit")
    actions = input("Choose actions: \n")
    if actions == 'refill':
        wallet.refill = float(input("Enter sum for refill: "))
        wallet.balance += wallet.refill
    elif actions == 'withdraw':
        print("Category <----------> ")
        print("game")
        print("entertainment")
        print("meal")
        print("other")
        category = input("Choose category: ")
        if category == 'game':
            wallet.ctg[0] = float(input("Enter a sum for withdraw in category game: "))
            wallet.balance -= wallet.ctg[0]
        elif category == 'entertainment':
            wallet.ctg[1] = float(input("Enter a sum for withdraw in category entertainment: "))
            wallet.balance -= wallet.ctg[1]
        elif category == 'meal':
            wallet.ctg[2] = float(input("Enter a sum for withdraw in category meal: "))
            wallet.balance -= wallet.ctg[2]
        elif category == 'other':
            wallet.ctg[3] = float(input("Enter a sum for withdraw in category other: "))
            wallet.balance -= wallet.ctg[3]
        else:
            print("Error")
    elif actions == 'report':
        print("Your balance %.2f $" % wallet.balance)
        print("You refill for: %.2f $" % wallet.refill)
        print("You withdraw for a category: ")
        print("     For game: %.2f $" % wallet.ctg[0])
        print("     For entertainment: %.2f $" % wallet.ctg[1])
        print("     For meal: %.2f  $" % wallet.ctg[2])
        print("     For other: %.2f  $" % wallet.ctg[3])
    elif actions == 'balance':
        print(wallet.balance)
    elif actions == 'exit':
        break
    else:
        print("Error choose another actions")
