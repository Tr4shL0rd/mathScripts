import numpy as np
from fractions import Fraction

try:
	def main():
		loop = True
		while loop:
			#brøk 1
			fraction1 = int(input("tæller1 = "))#1
			fraction2 = int(input("nævner1 = "))#6
			#brøk 2
			fraction3 = int(input("tæller2 = "))#3
			fraction4 = int(input("nævner2 = "))#4
			#find fælles nævner
			fractions_list=[Fraction(fraction1,fraction2),Fraction(fraction3,fraction4)]
			lcm = np.lcm.reduce([fr.denominator for fr in fractions_list])
			vals = [int(fr.numerator * lcm / fr.denominator) for fr in fractions_list]
			vals.append(lcm)
			#udregner brøk
			brøkTop1 = fraction1 * fraction4
			brøkBot1 = fraction2 * fraction4
			brøkTop2 = fraction3 * fraction2
			brøkBot2 = fraction4 * fraction2
			#forkorter brøk
			langBrøkTopS1 = brøkTop1 + brøkTop2
			langBrøkBotS1 = fraction2 * fraction4
			res = Fraction(langBrøkTopS1,langBrøkBotS1)
			#giver resultat
			print(f"{res}\n")
	main()
except KeyboardInterrupt:
	print("goodbye")