try:
	def main():
		l = True
		while l == True:
			sqrtX = int(input("x = "))#30
			
			result = sqrtX**3

			print(f"\nx = {result}\n======")			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")