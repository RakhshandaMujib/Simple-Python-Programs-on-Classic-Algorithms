def main():
	print("Enter the numbers in your list: (Enter any alphabet to stop)\n")
	list_is = []
	while True:
		element = input(" ")
		if element.lower().isalpha():
			break
		else:
			list_is.append(int(element))
	print(f"The elements are:\n\t{list_is}")

	for i in range(len(list_is)):
		if i != len(list_is)-1:
			print(f"\nPass {i+1}:")
		for j in range(len(list_is)-i-1):
			if list_is[j] > list_is[j+1]:
				list_is[j], list_is[j+1] = list_is[j+1], list_is[j]
			print(list_is)
	
if __name__ == '__main__':
	main()