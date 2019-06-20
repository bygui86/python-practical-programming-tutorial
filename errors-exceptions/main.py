
while True:
    try:
        print("Give me a number:")
        user = int(input())
        if user < 0:
            raise ValueError("Please give me a positive number!")
        else:
            print("The number was: %s" % user)
    except ValueError as e:
        print(e)
    finally:
        print("Try another time ;)")
        print("")