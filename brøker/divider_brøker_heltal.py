from fractions import Fraction
def main():
	while True:
		tæller = int(input("Tæller = "))
		nævner = int(input("Nævner = "))
		heltal = int(input("Heltal = "))

		top = tæller
		bot = nævner * heltal

		print(f"kort = {Fraction(top,bot)}")
		print(f"lang = {top}/{bot}")
		print()
main()