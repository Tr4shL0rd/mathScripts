#https://www.matematikfessor.dk/lessons/funktionsvaerdi-for-udtryk-med-kvadratrod-1203?id=21391484
import math
try:
	def main():
		while True:
			print("f(x) = a * math.sqrt(x)")
			x = int(input("x = "))
			a = int(input("a = "))
			print(a *math.sqrt(x))
			print()

	main()

except KeyboardInterrupt:
	print("CTRL-C\nGoodBye")