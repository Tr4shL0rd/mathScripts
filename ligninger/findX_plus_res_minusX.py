try:
	def main():
		l = True
		while l == True:
			a 	= int(input("a = "))#4
			b   = int(input("b = "))#17
			res = int(input("res = "))#47
			c 	= int(input("c = "))#2

			a = a+c
			res = res-b
			result = res/a
			print(f"\nx = {result}\n======")
			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")