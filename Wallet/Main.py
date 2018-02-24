class Wallet:
    balance = 130


wallet = Wallet()
print("refill")
print("withdraw")
print("report")
print("balance")
print("end")
while True:
    actions = input("Choose actions: ")
    if actions == 'refill':
        print("okey")
    elif actions == 'withdraw':
        print("")
    elif actions == 'report':
        print("")
    elif actions == 'balance':
        print(wallet.balance)
    elif actions == 'end':
        break
    else:
        print("Error choose another actions")
