#https://www.matematikfessor.dk/lessons/funktionsvaerdi-for-lineaert-udtryk-3-1199?id=21391447
try:
	while True:
		print("f(x) = a*x-b")
		x = int(input("x = "))
		a = int(input("a = "))
		b = int(input("b = "))

		print(a*x-b)
		print()
except KeyboardInterrupt:
	print("CTRL-C\r\tGood-Bye")