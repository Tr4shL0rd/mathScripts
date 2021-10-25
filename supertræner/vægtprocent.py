try:
    def main():
        while True:
            a = int(input("g = "))
            b = int(input("mg = "))/1000

            res = b/a*100
            print(f"\nvægtProcent = {round(res,2)}%\n===========\n")
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")