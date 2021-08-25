#https://www.matematikfessor.dk/lessons/uaegte-brok-531?id=21406056
try:
	def main():
		print("False == Uægte\nTrue == Ægte")
		while True:
			ægte = False
			a = int(input("a = "))
			b = int(input("b = "))

			if a > b:
				print("UÆGTE")
			else:
				ægte = True
				print("ÆGTE")
			print()
	main()
except KeyboardInterrupt:
	print("\nCTRL-C")
