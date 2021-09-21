try:
	def main():
		l = True
		while l == True:
			a 	= int(input("a = "))#10
			b   = int(input("b = "))#2
			res = int(input("x = "))#78


			res = res+b
			result = res/a


			print(f"\nx = {result}\n======")			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")