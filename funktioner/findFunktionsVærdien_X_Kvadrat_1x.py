#https://www.matematikfessor.dk/lessons/funktionsvaerdi-for-kvadratisk-udtryk-1-1200?id=21391478
try:
	def main():
		while True:
			print("f(x) = x**2+b")
			x = int(input("x = "))
			b = int(input("b = "))

			print(x**2+b)
			print()
	main()
except KeyboardInterrupt:
	print("\nCTRL-C\n\tGood-Bye")
except ValueError:
	print("something went wrong!?\n")
	main()