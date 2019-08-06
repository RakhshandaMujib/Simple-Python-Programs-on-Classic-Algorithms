def main():
	#Reading the elements:
	list_is = input("Enter the numbers in your list (separated by spaces):\n").split()
	list_is = [int(item) for item in list_is]
	print(f"The elements are:\n\t{list_is}")

	#Sorting the list:
	for i in range(1, len(list_is)):
		mark = i #Setting the mark. This implies the sorted list starts from 0 
					#and ends at the ith index.
		print(f"\nPass {i}:\nChecking for {list_is[i]}...")
		for j in range(mark-1,-1,-1):
			if list_is[mark] <= list_is[j]:
				list_is[mark], list_is[j] = list_is[j], list_is[mark])
				mark -= 1
			print(f"\t{list_is}")

if __name__ == '__main__':
	main()
