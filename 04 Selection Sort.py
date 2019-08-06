def main():
	#Reading the elements:
	list_is = input("Enter the numbers in your list (separated by spaces):\n").split()
	list_is = [int(item) for item in list_is]
	print(f"The elements are:\n\t{list_is}")

	#Sorting the list
	for i in range(len(list_is)):
		small = i #Setting the index with the smallest element.
		print(f"\nPass {i+1}:")
		for j in range(i+1,len(list_is)): #Finding the smallest element.
			small = j if list_is[j] <= list_is[small] else small
		list_is[i], list_is[small] = list_is[small], list_is[i] #Swapping.
		print(list_is)

if __name__ == '__main__':
	main()
