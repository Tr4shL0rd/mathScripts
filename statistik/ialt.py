#!/usr/bin/env python
try:
    from pyperclip import copy        
    def main():
        while True:
            nums = input("nums = ").strip().split(" ")
            nums = list(map(int, nums))
            #index = nums[index - 1]
            all = sum(nums)
            res = all#(index/all)*100
            copy(all)
            print(f"res = {res}\n==========\n")

            

    main()

except KeyboardInterrupt:
    print("goodbye!")