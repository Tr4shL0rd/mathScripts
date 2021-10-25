import math
def main():
	while True:
		log = True
		a 	 = int(input("a = "))
		b 	 = int(input("b = "))
		x    = int(input("x = "))

		try:
			xLog = math.log(x/a) / math.log(b)
		except ZeroDivisionError:
			xLog = 0
			log = False
		x = a*b**x

		if x > 99999:
			pass
			print()
		else:
			print(f"\nNo Log: {x = }")
		if log == False:
			pass
			print()
		else:
			print(f"With Log: {xLog = }\n======\n")
		
try:
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")