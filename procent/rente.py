try:
    import pyperclip
    def main():
        while True:
            r = float(input("r% = "))/100#0.05
            kr = int(input("kr = "))#100)
            noRente = r*kr
            yesRente = kr+noRente
            print(f"\nkun rente = {noRente}")
            print(f"alle penge + rente = {yesRente}\n======\n")

            pyperclip.copy(yesRente)
    main()
except KeyboardInterrupt:
    print("goodbye!!")
