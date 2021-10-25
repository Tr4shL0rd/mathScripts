#!/usr/bin/env python
try:
    from pyperclip import copy
    def cm3ToLiter(cm3):
        ...
        #en liter = 1000cm³
        return cm3/1000

    def main():
        while True:
            l = int(input("l = "))
            b = int(input("b = "))
            h = int(input("h = "))
            print(f"litter = {cm3ToLiter(l*b*h)} L\n=========\n")
            copy(cm3ToLiter(l*b*h))
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")