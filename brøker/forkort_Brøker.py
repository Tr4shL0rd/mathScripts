#https://www.matematikfessor.dk/lessons/forkort-en-brok-525?id=21406063
try:
	def main():
		while True:
			x = int(input("forkort brøken med: "))
			a = int(input("a = "))
			b = int(input("b = "))

			a = a/x
			b = b/x
			print("{}/{}\n".format(a,b))
	main()
except KeyboardInterrupt:
	print("\nGoodbye")