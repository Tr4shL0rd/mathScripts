from fractions import Fraction

try:
	def main():
		while True:

			tæller1 = int(input("Tæller1 = "))
			nævner1 = int(input("Nævner1 = "))

			tæller2 = int(input("Tæller2 = "))
			nævner2 = int(input("Nævner2 = "))

			topBrøk = tæller1 * tæller2
			botBrøk = nævner1 * nævner2
			resLong = f"Lang = {topBrøk}/{botBrøk}"
			resShort = f"Kort = {Fraction(topBrøk,botBrøk)}"
			if resLong != resShort:
				print(resShort, "\n")
				main()
			else:
				print(resLong,"\n")
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")