try:
    def main():
        while True:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))

            res = a * b / c

            print(f"\nres = {res}\n============\n")
    main()
except KeyboardInterrupt:
    print("\ngoodbye!")
