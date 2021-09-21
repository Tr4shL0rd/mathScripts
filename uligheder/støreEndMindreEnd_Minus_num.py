try:
    def main():
        while True:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            
            b = b+c
            result = b/a
            
            print(f"\nx = {result}\n======")
    main()

except KeyboardInterrupt:
    print("\nGoodBye!!")