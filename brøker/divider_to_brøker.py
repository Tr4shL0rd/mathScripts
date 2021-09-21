from fractions import Fraction
try:
	def main():
		while True:
			tæller1 = int(input("Tæller1 = "))
			nævner1 = int(input("Nævner1 = "))

			tæller2 = int(input("Tæller2 = "))
			nævner2 = int(input("Nævner2 = "))

			topBrøk = tæller1 * nævner2
			botBrøk = tæller2 * nævner1
			print(Fraction(topBrøk, botBrøk),"\n")
			



	main()
except KeyboardInterrupt:
	print()