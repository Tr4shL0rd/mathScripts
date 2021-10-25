try:
    from pyperclip import copy
    def main():
        while True:
            promille = float(input("promille = "))
            kr       = int(input("kr = "))

            topBrøk = promille*kr
            botBørk = 1000
            result = topBrøk/botBørk
            print(f"\nkr = {result}\n======\n")
            copy(result)

    main()
except KeyboardInterrupt:
    print("goodbye!")    