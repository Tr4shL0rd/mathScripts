#!/usr/bin/env python
#test 120/180
try:
	def main():
		while True:		
			a = int(input("a = "))#18
			b = int(input("b = "))#24

			for i in range(1,1001):
				if a % i == 0 and b % i == 0:
					a = a/i
					b = b/i
					print(i)
					print("{}/{}\n".format(a, b))
	main()
except KeyboardInterrupt:
	print("\nGood-bye")