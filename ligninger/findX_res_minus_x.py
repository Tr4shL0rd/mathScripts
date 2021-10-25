
try:
	def main():
		l = True
		while l == True:
			a 	= int(input("a = "))#3
			res = int(input("res = "))#104
			c 	= int(input("c = "))#10

			a = a+c
			result = res/a

			print(f"\nx = {result}\n======")
			
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")