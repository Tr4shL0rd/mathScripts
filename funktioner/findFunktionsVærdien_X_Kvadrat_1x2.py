#https://www.matematikfessor.dk/lessons/funktionsvaerdi-for-kvadratisk-udtryk-3-1202?id=21391482
try:
	def main():
		while True:
			print("f(x) = a*x**2 ")
			x = int(input("x = "))
			a = int(input("a = "))

			print(a*x**2)
			print()
	main()
except KeyboardInterrupt:
	print("\nCTRL-C\n\tGood-Bye")
except ValueError:
	print("something went wrong!?\n")
	main()