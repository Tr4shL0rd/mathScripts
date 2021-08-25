#!/usr/bin/env python
try:
	def main():
		while True:		
			a = int(input("a = "))#18
			b = int(input("b = "))#24

			for i in range(1,b):
				if a % i == 0 and b % i == 0:
					a = a/i
					b = b/i
			print("{}/{}".format(a, b))
	main()
except KeyboardInterrupt:
	print("\nGood-bye")