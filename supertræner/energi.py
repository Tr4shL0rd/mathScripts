try:
    def to_p(g:float, all:float):
        return round(g/all*100,1)
    def protein_kj(p:float):
        return 17 * p
    def fedt_kj(f:float):
        return 37 * f

    def main():
        while True:
            alt = float(input("kJ i alt = "))
            g = float(input("g = "))

            print(f"protein/kulhydrat = {protein_kj(g)}kJ")
            print(f"fedt = {fedt_kj(g)}kJ\n")
            print(f"fedtkJ% = {to_p(fedt_kj(g),alt)}%")
            print(f"protein/kulhydrat kJ% = {to_p(protein_kj(g),alt)}%\n=========\n")

    main()
except KeyboardInterrupt:
    print("\nGoodbye!")