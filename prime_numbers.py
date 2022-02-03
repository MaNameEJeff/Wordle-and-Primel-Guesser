def SieveOfEratosthenes(n):

	numbers = list(range(2, n))
	p = 2
	prime = []

	while(p*p <= n):
		for number in numbers[numbers.index(p)+1:]:
			if(number%p == 0):
				numbers[numbers.index(number)] = 0

		for number in numbers[numbers.index(p)+1:]:
			if(number != 0):
				p = number
				break

	for n in numbers:
		if((n != 0) and (len(str(n)) == 5)):
			prime.append(n)

	print(prime)

if __name__ == '__main__':
	n = 99999
	SieveOfEratosthenes(n)