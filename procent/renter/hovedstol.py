try:
    from math import pow
    def main():
        while True:
            H = int(input("Hovedstol = ")) 
            P = float(input("procent = "))/100
            n = int(input("år = "))
            PmedPlus = P+1
            p = PmedPlus**-n
            p = 1-p
            res = P/p * H
            print(f"\nres = {round(res,2)}\n======\n")


    main()
except KeyboardInterrupt:
    print("goodbye!!")