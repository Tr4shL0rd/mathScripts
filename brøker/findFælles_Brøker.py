try:
	def main():
		while True:
			b1 = int(input("nævner Brøker1 = "))
			b2 = int(input("nævner Brøker2 = "))
			resultat = b1*b2
			print(f"{resultat = }\n")
			
	main()
except KeyboardInterrupt:
	print("goodbye")