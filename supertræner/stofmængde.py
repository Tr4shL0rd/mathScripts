try:
    def main():
        while True:
            a = int(input("g = "))
            b = int(input("mg = "))

            res = b/a*100
            print(f"vægtProcent = {round(res,2)}\n===========\n")
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")