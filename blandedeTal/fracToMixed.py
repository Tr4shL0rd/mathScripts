def main():
	num = int(input("Numerator: "))
	dem = int(input("Denominator: "))

	a = num // dem
	b = num % dem
	print("The mixed number is {} and {}/{}".format(a, b, dem))


main()