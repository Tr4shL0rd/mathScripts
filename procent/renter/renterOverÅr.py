try:
    from decimal import Decimal
    from pyperclip import copy
    def main():
        while True:
            k = Decimal(input("kr = "))#Decimal(5000)
            r = Decimal(input("rente = "))/100#Decimal(3/100)
            try:
                n = int(input("år = "))#Decimal(12)
            except ValueError:
                n = 1
            kn = Decimal(round(k*(1+r)**n,2))
            print(f"\nkun rente = {r*k}")
            print(f"Penge efter {n} år = {kn}\n======\n")
            copy(float(kn))
    main()
except KeyboardInterrupt:
    print("goodbye!!")