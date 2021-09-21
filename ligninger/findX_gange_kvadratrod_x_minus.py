try:
	def main():
		l = True
		while l == True:
			a 	  = int(input("a = "))#3
			sqrtX = int(input("x = "))#30
			b 	  = int(input("b = "))#3
			
			ress = sqrtX-b
			ress = ress/a
			result = ress**2


			print(f"\nx = {result}\n======")			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")