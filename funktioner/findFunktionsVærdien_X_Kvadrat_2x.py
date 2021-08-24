#https://www.matematikfessor.dk/lessons/funktionsvaerdi-for-kvadratisk-udtryk-2-1201?id=21391480
try:
	def main():
		while True:
			print("f(x) = x**2+b*x")
			x = int(input("x = "))
			b = int(input("b = "))

			print(x**2+b*x)
			print()
	main()
except KeyboardInterrupt:
	print("\nCTRL-C\n\tGood-Bye")
except ValueError:
	print("something went wrong!?\n")
	main()