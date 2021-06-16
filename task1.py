print("Enter the number")
number = int(input())
if number > 7:
    print("Hello")
else:
    while number <= 7:
        print("Try again")
        print("Enter the number")
        number = int(input())
        if number > 7:
            print("Hello")


