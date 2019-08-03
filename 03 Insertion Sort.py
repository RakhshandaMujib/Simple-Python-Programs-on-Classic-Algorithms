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

	#Sorting the list:
	for i in range(1, len(list_is)):
		mark = i #Setting the mark. This implies the sorted list starts from 0 
					#and ends at the ith index.
		print(f"\nPass {i}:\nChecking for {list_is[i]}...")
		for j in range(mark-1,-1,-1):
			if list_is[mark] <= list_is[j]:
				list_is[mark], list_is[j] = swap(list_is[mark], list_is[j])
				mark -= 1
			print(f"\t{list_is}")

def swap(x, y):
	'''
	Returns the swapped values of x and y.
	'''
	x = x+y
	y = x-y
	x = x-y
	return (x,y)

if __name__ == '__main__':
	main()