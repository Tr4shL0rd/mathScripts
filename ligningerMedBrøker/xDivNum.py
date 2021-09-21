try:
	def main():
		while True:
			a = int(input("a = "))
			res = int(input("res = "))

			for result in range(1001):
				if result / a == res:
					print(f"\nx = {result}\n======")	
	main()
except KeyboardInterrupt:
	print("\nGoodBye!")