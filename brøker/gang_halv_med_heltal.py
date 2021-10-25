from math import floor
import pyperclip
try:
	def main():
		while True:
			nævner = int(input("Nævner = "))
			tæller = int(input("Tæller = "))
			heltal = int(input("Heltal = "))
			topBrøk = nævner * heltal
			res = topBrøk / tæller
			res = floor(res)
			pyperclip.copy(res)
			print(f"{res}\n")
	main()
except KeyboardInterrupt:
	print("\bGoodBye!")