#!/usr/bin/env python
try:
    from pyperclip import copy
    def checkCM(l,b,h):
            

        if "dm" in l:
            return "at l"
        elif " dm" in b:
            return "at b"
        elif " dm" in h:
            return "at h"
    def main():
        while True:
            l = input("l = ").strip()
            b = input("b = ").strip()
            h = input("h = ").strip()
            print(checkCM(l,b,h))
            #print(l.replace(" dm",""))
            #print(f"litter = {l*b*h} L\n=========\n")
            #copy(dmToLiter(l*b*h))
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")