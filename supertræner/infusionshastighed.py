try:
    def main():
        while True:
            a = int(input("ml = "))
            b = int(input("tid = "))

            res = a/b
            print(f"\ninfusionshastigheden = {res}ml/time\n===========\n")
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")