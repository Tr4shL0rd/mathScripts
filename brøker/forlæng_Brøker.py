#https://www.matematikfessor.dk/lessons/forlaeng-en-brok-526?id=21406060
try:
	def main():
		while True:
			x = int(input("Forlæng brøken med: "))
			a = int(input("a = "))
			b = int(input("b = "))

			a = a*x
			b = b*x
			print("{}/{}\n".format(a,b))
	main()
except KeyboardInterrupt:
	print("\nGoodbye")