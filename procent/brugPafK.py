import pyperclip
try:
    def main():
        while True:
            procent = int(input("procent = "))#90#
            kroner  = int(input("kroner = "))#1000#

            step1 = procent/100
            step2 = step1*kroner
            result = kroner-step2
            print(f"\nx = {result}\n======")
            pyperclip.copy(result)
    
except KeyboardInterrupt:
    print("\nGoodBye!!")
main()