#Reading the elements of a list globally:
lst = input("Enter the numbers in your list (separated by spaces):\n").split()
lst = [int(item) for item in lst]

def main():
	quick_sort(lst, 0, len(lst)-1)
	print(f"Sorted list is:\n\t{lst}")

def get_pivot(lst, low, high):
	'''
	Arguments:
		lst - (list) The list of which we want to find the pivot.
		low - (int) Index of the list from where we want to start.
		high - (int) Index of the list at which we want to end.
	Returns:
		The median of the values at high, low and middle index positions.
		This ensures O(log(n)) time complexity.
	'''
	mid = int((high + low) / 2) 
	median = 0
	l, h, m = lst[low], lst[high], lst[mid]

	if (l < h or l < m) and (l >= h or l >= m):
		median = low 
	elif (h < l or h < m) and (h >= l or h >= m):
		median = high 
	elif (m < h or m < l) and (m >= h or m >= l):
		median = mid
	return median

def partition(lst, low, high):
	'''
	Arguments:
		lst - (list) The list of which we want to find the pivot.
		low - (int) Index of the list from where we want to start.
		high - (int) Index of the list at which we want to end.

	Returns:
		The index position of the pivot such that all the values to left of it
		is lesser and all the values to the right of it is greater than it. 
	'''
	pivot = get_pivot(lst, low, high)
	pivot_val = lst[pivot]
	print("Partitioning the list") 
	print(f"{lst} from {low} to {high} with pivot {pivot_val}:")

	#Pushing the pivot to the start of the list.
	lst[low], lst[pivot] = lst[pivot], lst[low] 

	#Setting border index. 
	border = low + 1 

	#Pushing every element that's lesser than the pivot to its left. 
	for current in range(low, len(lst)):
		if lst[current] < pivot_val:
			print(lst)
			lst[border], lst[current] = lst[current], lst[border]
			border += 1
	lst[border-1], lst[low] = lst[low], lst[border-1]

	print(f"{lst}\n")
	return(border)

def quick_sort(lst, low, high):
	#Checking if the list length is greater than 1. 
	if low < high: 
		part_from = partition(lst, low, high)
		quick_sort(lst, low, part_from-1)
		quick_sort(lst, part_from+1, high)

if __name__ == '__main__':
	main()