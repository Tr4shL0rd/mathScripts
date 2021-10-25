try:
    def main():
        while True:
            mgml = int(input("mg/ml = "))
            mg   = int(input("ml pr. dosis = "))

            res = mg/mgml
            print(f"væske = {res}ml\n==========\n")
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")