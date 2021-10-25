#!/usr/bin/env python
try:
    from pyperclip import copy
    def main():
        while True:
            h = float(input("h = "))
            g = float(input("g = "))

            res = 1/2*h*g
            print(f"areal = {res}\n=========\n")
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")