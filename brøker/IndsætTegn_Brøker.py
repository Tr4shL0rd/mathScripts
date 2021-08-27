try:
	def main():
		loop = True
		while loop == True:
			Lfrac1 = int(input("Tæller1 = "))#1
			Lfrac2 = int(input("Nævner1 = "))#2
			
			Rfrac1 = int(input("Tæller2 = "))#2
			Rfrac2 = int(input("Nævner2 = "))#5

			checkFrac1 = int(input("Tæller3 = "))#8
			checkFrac2 = int(input("Nævner3 = "))#10

			Lfrac_1 = Lfrac1 * Rfrac2
			Lfrac_2 = Lfrac2 * Rfrac2
			
			Rfrac_1 = Rfrac1 * Lfrac2
			Rfrac_2 = Rfrac2 * Lfrac2

			print(f"frac1: {Lfrac_1}/{Lfrac_2}")
			print(f"frac2: {Rfrac_1}/{Rfrac_2}")
			fracTop = Lfrac_1 + Rfrac_1
			fracBot = Lfrac_2 
			print(f"{fracTop}/{fracBot}")
			loop = False
	main()
except KeyboardInterrupt:
	print("")