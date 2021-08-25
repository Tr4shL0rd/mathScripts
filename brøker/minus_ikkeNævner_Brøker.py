try:
	def main():
		while True:
			a1 = int(input("tæller1 = "))
			b1 = int(input("nævner1 = "))
			
			a2 = int(input("tæller2 = "))
			b2 = int(input("nævner2 = "))

			tæller1 = a1*b2
			nævner1 = a2*b2

			tæller2 = a2*b1
			nævner2 = b2*b1
			#print(f"{tæller1}/{nævner1}")

			topBrøker = tæller1 - tæller2
			botBrøker = nævner2
			print(f"{topBrøker}/{botBrøker}\n")

	main()
except KeyboardInterrupt:
	print("goodbye")