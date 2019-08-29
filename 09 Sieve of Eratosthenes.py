def sieve_of_Eratosthenes(upper_limit):
	'''
	This method will print all the prime numbers up to 
	the user-given upper limt using the algorithm of
	Sieve of Erastosthenes.
	Argument(s):
	upper_limit - Integer. The user-given upper bound.
	'''
	#We assume that all the numbers from 0 to upper_limit
	#are prime. Thus, we first create a list of only boolean values,
	#initially all True to start with the seiving process.
	is_prime = [True for number in range(upper_limit)] 
	prime = 2 #The first prime number. 
	while prime**2 < upper_limit: #Till the square of the current prime
								  #is lesser than upper_limit... 
		if is_prime[prime]: #If the current prime number hasn't been 
							#marked False during the looping...
			for multiple in range(prime**2, upper_limit, prime):
				is_prime[multiple] = False #Mark out all the multiples
										   #of the current prime.
		prime += 1 
	for number in range(2, upper_limit): #Omitting 0 and 1.
		if is_prime[number]: #If the number is prime...
			print(number)

def main():
	ul = int(input('Enter the upper limit:')) + 1
	sieve_of_Eratosthenes(ul)

if __name__ == '__main__':
	main()