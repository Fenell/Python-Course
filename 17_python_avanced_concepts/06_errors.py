while True:
    try:
        a = int(input("Enter num 1: "))
        b = int(input("Enter num 2: "))
        rsl = a + b
        print("The sum ", rsl)
    except Exception as e:
        print("something went wrong", e)
