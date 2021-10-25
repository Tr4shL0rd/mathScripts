try:
    import pyperclip
    def main():
        while True:
            kroner = int(input("Kroner = "))#90#
            moms = 1.25

            result = kroner/moms
            print(f"\npris = {result}\n======")
            pyperclip.copy(result)
    
except KeyboardInterrupt:
    print("\nGoodBye!!")
main()