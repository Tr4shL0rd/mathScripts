try:
	def main():
		while True:
			heltal = int(input("heltal = "))
			tæller = int(input("Tæller = "))
			nævner = int(input("Nævner = "))

			topBrøk = heltal
			botBrøk = tæller/nævner
			print(f"{topBrøk / botBrøk}")
	main()
except KeyboardInterrupt:
	print()