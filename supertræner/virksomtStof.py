try:
    def main():
        while True:
            mg = int(input("mg = "))
            ml = int(input("ml = "))

            s = mg/ml
            print(f"S = {s}mg/ml\n===========\n")
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")