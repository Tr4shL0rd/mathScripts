from fractions import Fraction

try:
	def main():
		while True:
			heltal = int(input("Heltal = "))
			tæller = int(input("Tæller = "))
			nævner = int(input("Nævner = "))

			topBrøk = heltal * tæller
			botBrøk = nævner
			print(f"Lang = {topBrøk}/{botBrøk}")
			print(f"Kort = {Fraction(topBrøk,botBrøk)}\n")
	main()
except KeyboardInterrupt:
	print("\nGoodbye!")