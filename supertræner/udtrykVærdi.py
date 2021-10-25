try:
    def main():
        while True:
            firstNum = int(input("1. tal = "))
            a = int(input("a = "))
            b = int(input("b = "))
            lastNum = int(input("sidste tal = "))

            res = firstNum * (a-b) + lastNum
            print(f"res = {res}\n============\n")
    main()
except KeyboardInterrupt:
    print("\ngoodbye!")
