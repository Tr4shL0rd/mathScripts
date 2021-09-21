try:
	def main():
		while True:
			a = int(input("a = "))#20
			res = int(input("res = "))#4

			result = a/res
			print(f"\nx = {result}\n======")	
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")