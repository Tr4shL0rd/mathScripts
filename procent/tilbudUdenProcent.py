import pyperclip
try:
    def main():
        print("main")
        while True:
            gp = int(input("gammel Pris = "))
            np = int(input("Ny Pris = "))

            gpTop = gp-np
            gpBot = gp
            result = gpTop/gpBot*100

            print(f"\nx = {result}\n======")
            pyperclip.copy(result)
    
except KeyboardInterrupt:
    print("\nGoodBye!!")
main()