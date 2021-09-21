try:
	def main():
		l = True
		while l == True:
			a 	  = int(input("a = "))#9
			x = int(input("x = "))#45
			
			ress = x/a
			result = ress**3

			print(f"\nx = {result}\n======")			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")