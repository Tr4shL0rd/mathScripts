#https://www.matematikfessor.dk/lessons/funktionsvaerdi-for-lineaert-udtryk-2-1198?id=21391446
try:
	def main():
		while True:
			print("f(x) = a*x+b")
			x = int(input("x = "))
			a = int(input("a = "))
			b = int(input("b = "))

			print(a*x+b)
			print()
	main()
except KeyboardInterrupt:
	print("CTRL-C\r\tGood-Bye")
except ValueError:
	print("something went wrong!?\n")
	main()