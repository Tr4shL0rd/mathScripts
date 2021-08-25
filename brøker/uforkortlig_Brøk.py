from fractions import Fraction
try:
	def main():
		while True:
			a = int(input("a = "))
			b = int(input("b = "))

			print(Fraction(a,b),"\n")
	main()
except KeyboardInterrupt:
	print("goodbye")