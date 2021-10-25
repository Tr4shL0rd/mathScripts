#!/usr/bin/env python
try:
    from pyperclip import copy
    def dmToLiter(dm):
        ...
        #en liter = 1000cm³
        return dm

    def main():
        while True:
            l = int(input("l = "))
            b = int(input("b = "))
            h = int(input("h = "))
            print(f"litter = {dmToLiter(l*b*h)} L\n=========\n")
            copy(dmToLiter(l*b*h))
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")