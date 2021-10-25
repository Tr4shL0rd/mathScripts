try:
    def main():
        while True:
            a   = int(input("a = "))
            b   = int(input("b = "))
            c   = int(input("c = "))
            res = int(input("res = "))

            step1 = c*res
            step2 = step1-b
            result = step2/a
            print(f"\nx = {result}\n======")

    main()
except KeyboardInterrupt:
    print("\nGoodbye")