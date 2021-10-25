import sys
def main():
    print("main")
    try:
        while True:
            a = int(input("a = "))
            b = int(input("b = "))
            result = b/a
            print(f"\nx = {result}\n======")
    except KeyboardInterrupt:
        print("\nGoodBye!!")

def minus():
    print("minus")
    try:
        while True:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            b = b+c
            result = b/a
            print(f"\nx = {result}\n======")
    except KeyboardInterrupt:
        print("\nGoodBye!!")
def plus():
    print("plus")
    try:
        while True:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            
            b = c-b
            result = b/a
            
            print(f"\nx = {result}\n======")
    except KeyboardInterrupt:
        print("\nGoodBye!!")
def floats():
    print("main")
    try:
        while True:
            a = float(input("a = "))
            b = float(input("b = "))
            result = b/a
            print(f"\nx = {result}\n======")
    except KeyboardInterrupt:
        print("\nGoodBye!!")

try:
    if sys.argv[1] == "-p" or sys.argv[1] == "-plus":
        plus()
    elif sys.argv[1] == "-m" or sys.argv[1] == "-minus":
        minus()
    elif sys.argv[1] == "-f" or sys.argv[1] == "-floats":
        floats()
    else:
        main()
except KeyboardInterrupt:
    print("\nGoodBye!!")
except IndexError:
    main()
