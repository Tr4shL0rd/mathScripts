try:
    from sys import path
    path.insert(0, '../')
    
    from lib import helper
    
    #def toList(string):
    #    return string.strip().split(" ")
    def main():
        while True:
            b = helper.toList(input("Bogstaver: "))
            tal = helper.toList(input("Tal: ")) 
            #helper.sumOfStrList(tal)
            #res = 2*(a+b)
            #print(f"{res}\n==========\n")
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("goodbye!")