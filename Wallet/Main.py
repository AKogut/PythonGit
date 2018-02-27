class Wallet:
    balance = 130
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
    print("end")
    actions = input("Choose actions: \n")
    if actions == 'refill':
        refill = float(input("Enter sum for refill: "))
        wallet.balance += refill
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
        else:
            print("Error")

    elif actions == 'report':
        print("")
    elif actions == 'balance':
        print(wallet.balance)
    elif actions == 'exit':
        break
    else:
        print("Error choose another actions")
