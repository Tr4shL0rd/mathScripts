
try:
	def main():
		l = True
		while l == True:
			#a * (aP1 - bP1) = b + c
			a 	= int(input("a = "))#3
			aP1 = int(input("aP1 = "))#2
			bP1 = int(input("bP1 = "))#1
			b 	= int(input("b = "))#2
			c   = int(input("c = "))#13

			a1 = a*aP1#6
			a2 = a*aP1-bP1*a#3

			a3 = a1-b#4

			ress = a2+c
			result = ress/a3
			print(f"\nx = {result}\n======")
			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")