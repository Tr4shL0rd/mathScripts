try:
	def main():
		while True:
			a 	= int(input("a = "))#3
			b   = int(input("b = "))#15
			res = int(input("res = "))#50
			c 	= int(input("c = "))#4

			a = a+c
			res = res-b
			result = res/a


			print(f"\nx = {result}\n======")
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")