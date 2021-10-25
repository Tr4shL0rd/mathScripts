try:
	def main():
		l = True
		while l == True:
			a 	= int(input("a = "))#5
			b   = int(input("b = "))#2
			res = int(input("x = "))#52


			res = res-b
			result = res/a


			print(f"\nx = {result}\n======")			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")