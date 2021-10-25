try:
    import pyperclip
    def main():
        while True:
            kroner = int(input("Kroner = "))#90#
            moms = 1.25

            udenMoms = kroner/moms
            result = kroner-udenMoms
            print(f"\npris = {result}\n======")
            pyperclip.copy(result)
    
except KeyboardInterrupt:
    print("\nGoodBye!!")
main()