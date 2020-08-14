def counting_sort(list_is, lower, upper):
	count = {i : 0 for i in range(lower, upper +1)}
	for i in range(len(list_is)):
		if list_is[i] > (upper + 1) or list_is[i] < lower:
			print(f'{list_is[i]} is not within [{lower},{upper}].')
			return
		elif list_is[i] in count:
			count[list_is[i]] += 1
	print('The sorted list is:')
	for i in count.items():
		print(f"{(str(i[0]) + ' ') * i[1]}", end = '')
	return

def main():
	lower, upper = map(int, input('Enter the lower and upper limit separated by space:\n').split())
	print("Enter the numbers in your list: (Enter any alphabet to stop)\n")
	list_is = []
	while True:
		element = input()
		if element.lower().isalpha():
			break
		else:
			list_is.append(int(element))
	print(f"The elements are:\n\t{list_is}")
	counting_sort(list_is, lower, upper)

if __name__ == '__main__':
	main()

		

