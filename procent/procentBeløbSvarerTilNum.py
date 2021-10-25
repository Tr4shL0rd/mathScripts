try:
    import pyperclip
    def main():
        while True:
            procent = int(input("procent = "))
            tal     = int(input("tal = "))


            result = tal/procent * 100
            print(f"\nx = {result}\n======")
            pyperclip.copy(result)
    
except KeyboardInterrupt:
    print("\nGoodBye!!")
main()