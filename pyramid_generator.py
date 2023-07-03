cont = "s"
print("Star pyramid generator.")
print()
while cont == "s":
    num = int(input("Enter a number : "))
    a = 0
    b = 1
    c = num

    while b < (num + 1):
        print(" " * c, end="")
        d = 0

        while d <= a:
            print("%", "", end="")
            d = d + 1

        b = b + 1
        a = a + 1
        c = c - 1
        print()

    cont = input("continue - enter 's', quit - enter 'q' : ").lower()
