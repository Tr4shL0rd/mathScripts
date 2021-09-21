try:
	def main():
		l = True
		while l == True:
			a 	= int(input("a = "))#7
			b   = int(input("b = "))#14
			res = int(input("x = "))#28

			b = res+b
			result = b/a
			result = result**3

			print(f"\nx = {result}\n======")			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")