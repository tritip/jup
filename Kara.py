from typing import Tuple


def Kara(X: str, Y: str) -> int:
	"""
	Multiply arbitratry length numbers X,Y efficiently using Karatsuba's algorithm
	Split each numberstring into left/right halves, X->a,b Y->a,c
	recursively divide and conquer.  
	
	Algorithm per course notes: x.y=(10^n*ac+10^n/2*(ad+bc))+bd
	"""

	def conform_digits(X: str, Y: str) -> Tuple:
		"Conform strings: zero pad for equal and even-numbered lengths"

		def is_odd(x: int) -> int:
			return x % 2 == 1

		l = max(len(X) + is_odd(len(X)), len(Y) + is_odd(len(Y)))
		return (X.zfill(l), Y.zfill(l))

	def shift10_left(n: int, places: int) -> int:
		"No-multiply version of n*10^places"

		return int(str(n) + '0' * places)

	X, Y = conform_digits(X, Y)
	iX, iY = int(X), int(Y)

	if iX <= 10 and iY <= 10:
		print(iX, iY)
		return iX * iY  # allow multiplication onlyin this simple case

	else:
		ndigits = len(X)
		split = ndigits // 2

		a, b, c, d = X[:split], X[split:], Y[:split], Y[split:]

		ac, ad = Kara(a, c), Kara(a, d)
		bc, bd = Kara(b, c), Kara(b, d)

		return shift10_left(ac, ndigits) + shift10_left((ad + bc), split) + bd


def main():

	X = "3141592653589793238462643383279502884197169399375105820974944592"
	Y = "2718281828459045235360287471352662497757247093699959574966967627"

	print(Kara(X, Y))


if __name__ == "__main__":
	main()
