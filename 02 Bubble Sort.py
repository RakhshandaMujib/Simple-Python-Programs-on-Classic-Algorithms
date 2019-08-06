def main():
	#Reading the elements:
	list_is = input("Enter the numbers in your list (separated by spaces):\n").split()
	list_is = [int(item) for item in list_is] 
	print(f"The elements are:\n\t{list_is}")
	
	#Sorting the list: 
	for i in range(len(list_is)):
		if i != len(list_is)-1:
			print(f"\nPass {i+1}:")
		for j in range(len(list_is)-i-1):
			if list_is[j] > list_is[j+1]:
				list_is[j], list_is[j+1] = list_is[j+1], list_is[j]
			print(list_is)
	
if __name__ == '__main__':
	main()
