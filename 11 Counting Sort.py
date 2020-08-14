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
	lower, upper = map(int, input('Enter the range (separated by space):\n').split())
	list_is = []
	list_is = input("Enter the numbers in your list (separated by spaces):\n").split()
	list_is = [int(item) for item in list_is]
	print(f"The elements are:\n\t{list_is}")
	counting_sort(list_is, lower, upper)

if __name__ == '__main__':
	main()

		

