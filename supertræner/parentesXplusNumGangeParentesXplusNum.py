try:
    def main():
        while True:
            a = int(input("a = "))
            b = int(input("b = "))
            x = "x"
            
            ab = a*b
            step1 = a + b + ab
            res = f"x\u00b2 {a + b}x + {ab}"

            print(f"\nres = {res}\n============\n")
    main()
except KeyboardInterrupt:
    print("\ngoodbye!")
