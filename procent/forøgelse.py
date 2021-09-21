import pyperclip
try:
    def main():
        print("main")
        while True:
            k = int(input("k = "))#korner#45000#
            p = int(input("p = "))#procent#10#
            
            step1f = p/100
            step2f = step1f * k
            nyLøn = k+step2f
            forøg = step2f;print(f"\nForøgelsen = {forøg}")
            print(f"Ny Løn = {nyLøn}\n======")
            
            #pyperclip.copy(result)
    
except KeyboardInterrupt:
    print("\nGoodBye!!")
main()