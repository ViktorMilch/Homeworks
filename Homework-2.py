while True:
    age = int(input("Enter your age"))
    name = input("Enter your name")

    if age >= 18:
        print("Hello,", name)
    else:
        print("Go sleep, little child, {}!!!".format(name))