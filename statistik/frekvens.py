#!/usr/bin/env python
try:
    from pyperclip import copy        
    def main():
        while True:
            index = int(input("index = "))
            nums = input("nums = ").strip().split(" ")
            nums = list(map(int, nums))
            index = nums[index - 1]
            all = sum(nums)
            #all = int(input("nums = "))
            res = (index/all)*100
            copy(res)
            print(f"res = {res}%\n==========\n")

            

    main()

except KeyboardInterrupt:
    print("goodbye!")