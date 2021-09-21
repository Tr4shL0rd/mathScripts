try:
    def main():
        print("main")
        while True:
            k = int(input("k = "))
            p = int(input("p = "))

            result = k*(1-p/100)
            print(f"\nx = {result}\n======")
    
    
except KeyboardInterrupt:
    print("\nGoodBye!!")
main()