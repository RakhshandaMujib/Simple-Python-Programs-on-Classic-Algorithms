def main():
    print("This program demonstrates the Collatz Conjecture.\n")
    num = int(input("Enter a number:\n\t"))
    if num <= 1:
        print("The number has to be greater than 1.")
    else: 
        print(f"{count_steps(num)} steps needed for {num} to go to 1.")
    
def count_steps(n):
    '''
    This method calculates the number of steps needed for a number to 
    reach the Collatz Conjecture.
    
    Argument:
    n - Integer. The number we're going to work with.
    Returns:
    count - Integer. Number of steps for n to reduce to 1.
    
    Do the following till n gets reduced to 1:
        If n is an even number we divide it by 2.
        If n is odd, multiply it by 3 and add 1.
    '''
    count = 0
    
    while n != 1:
        count += 1 #Count will be incremented irrespective of the nature 
                   #of number- odd or even.
        if n%2 == 0:
            n /= 2
        else:
            n = ((n*3) + 1)/2 #For every odd number n, 3n + 1 will be an even 
                              #number and every even number is to be 
                              #divided by 2. Thus, we can do both the steps at 
                              #once to speed up the process. 
            count += 1 #Incrementing count again as we do 2 steps simultaneously
                       #in case n is odd.
    
    return count

if __name__ == '__main__':
    main()