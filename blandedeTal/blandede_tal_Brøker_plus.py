from fractions import Fraction
try:
	def fracToMixed(num,dem):
		
		a = num // dem
		b = num % dem
		#print(a)
		print("{} {}/{}".format(a, b, dem))
		print()
		main()
	
	def gcd(a, b):
	    if (a == 0):
	        return b;
	    return gcd(b % a, a);

	def lowest(den3, num3):

	    common_factor = gcd(num3, den3);

	    den3 = int(den3 / common_factor);
	    num3 = int(num3 / common_factor);
	    #print(num3, "/", den3);
	    fracToMixed(num3,den3)

	def addFraction(num1, den1, num2, den2):

	    den3 = gcd(den1, den2);

	    den3 = (den1 * den2) / den3;

	    num3 = ((num1) * (den3 / den1) +
	            (num2) * (den3 / den2));

	    lowest(den3, num3);

	def main():
		loop = True
		while loop == True:
			heltal1 = int(input("heltal1 = "))#2
			tæller1 = int(input("tæller1 = "))#2
			nævner1 = int(input("nævner1 = "))#3

			heltal2 = int(input("heltal2 = "))#3
			tæller2 = int(input("tæller2 = "))#1
			nævner2 = int(input("nævner2 = "))#2


			brøkTop1 = heltal1 * nævner1 + tæller1
			brøkBot1 = nævner1
			
			brøkTop2 = heltal2 * nævner2 + tæller2
			brøkBot2 = nævner2
			#print(f"{brøkTop1} / {brøkBot1}")
			#print(f"{brøkTop2} / {brøkBot2}\n")
			addFraction(brøkTop1, brøkBot1, brøkTop2, brøkBot2)

			#loop = False
	main()
except KeyboardInterrupt:
	print("goodbye") 
