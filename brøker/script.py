from fractions import Fraction
def mixedNums(num,dem):
	#num = #int(input("Numerator: "))
	#dem = #int(input("Denominator: "))

	a = num // dem
	b = num % dem
	print("The mixed number is {} and {}/{}".format(a, b, dem))

def main():
	heltal1 = 1#3
	tæller1 = 1#1
	nævner1 = 4#4

	heltal2 = 2#3
	tæller2 = 1#1
	nævner2 = 5#8

	#topBrøk1 = heltal1 * nævner1 + tæller1
	#topBrøk2 = heltal2 * nævner2 + tæller2
	topBrøk1 = 1 * 4 + 1
	topBrøk2 = 2 * 5 + 1
	#botBrøk1 = nævner1
	#botBrøk2 = nævner2
	botBrøk1 = 4
	botBrøk2 = 5
	for j in range(1,1000000):
		for i in range(1,101):
			if 4 % i == j and 5 % i == j:		
				print(i)
				
	
	#topBrøk1 = topBrøk1 * i
	#botBrøk1 = botBrøk1 * i
	
	#topBrøk = topBrøk1 + topBrøk2
	#print(f"{topBrøk}/{botBrøk1}")
	#mixedNums(topBrøk, botBrøk1)


main()