try:
    def main():
        while True:
            a = int(input("a = "))#2
            b = int(input("b = "))#4
            res = int(input("res = "))#5
            b = res - b 
            result = a * b
            print(f"\nx = {result}\n======")
    main()
except KeyboardInterrupt:
    print("\nGoodBye!")