try:
    def l_to_ml(l:float):
        return l*1000
    def ul_to_ml(ul:int):
        return ul/1000
    def main():
        while True:
            l  = float(input("l = "))
            ul = int(input("μl = "))

            #print(ul/l)
            print(f"{l_to_ml(l)}\n{ul_to_ml(ul)}")
            #print()
            #print(f"\nPLACEHOLDER = {res}PLACEHOLDER\n===========\n")
            
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")