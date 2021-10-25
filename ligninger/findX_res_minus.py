try:
	def main():
		while True:
			a 	= int(input("a = "))#4
			res = int(input("res = "))#99
			b = int(input("b = "))#7

			a = a+b
			result = res/a

			print(f"\nx = {result}\n======")
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")