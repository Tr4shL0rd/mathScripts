try:
    def main():
        while True:
            a1 = int(input("a = "))#1
            b1 = int(input("b = "))#3
            a2 = int(input("a2 = "))#2
            
            side1 = b1 * a1/b1
            side2 = b1 * a2
            print(side2)            

            result=side2;print(f"\nx = {result}\n======")	
    main()
except KeyboardInterrupt:
	print("\nGoodBye!")