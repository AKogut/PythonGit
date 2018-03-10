
text = open('result.txt', 'w')
about = ['Name:', '', ' Surname:', '', '', 'year of birth ', '\n']
while True:
    print("<------------->")
    print("add")
    print("exit")
    actions = input("Enter actions: ")
    if actions == 'exit':
        text.close()
        break
    elif actions == 'add':
        about[1] = input("Enter name: ")
        about[3] = input("Enter surname: ")
        about[4] = input("Enter the year of birth: ")
        for i in range(0, 7):
            text.write("  ")
            text.write(about[i])
    else:
        print("Error")
