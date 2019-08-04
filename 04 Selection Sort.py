def main():
	#Reading and printing the list of numbers:
	print("Enter the numbers in your list: (Enter any alphabet to stop)\n")
	list_is = []
	while True:
		element = input(" ")
		if element.lower().isalpha():
			break
		else:
			list_is.append(int(element))
	print(f"The elements are:\n\t{list_is}")

	#Sorting the list
	for i in range(len(list_is)):
		small = i #Setting the index with the smallest element.
		print(f"\nPass {i+1}:")
		for j in range(i+1,len(list_is)): #Finding the smallest element.
			small = j if list_is[j] <= list_is[small] else small
		list_is[i], list_is[small] = swap(list_is[i], list_is[small]) #Swapping.
		print(list_is)

def swap(x,y):
	'''
	Returns the swapped values of x and y.
	'''
	x = x+y
	y = x-y
	x = x-y
	return(x,y)

if __name__ == '__main__':
	main()

