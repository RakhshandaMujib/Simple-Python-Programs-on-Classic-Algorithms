#Reading the elements of a list globally:
l = input("Enter the numbers in your list (separated by spaces):\n").split()
l = [int(item) for item in l]

def main():
	merge_sort(l, 0, len(l)-1)
	print(f"Sorted list is:\n\t{l}")

def merge_sort(l, low, high):
	'''
	This method is called recursively to break the unsorted list
	into slices of of sorted lists till the slice length is 1. 
	It then calls the merge() method to merge the sorted slices.

	Arguments:
	l - (list) The list to be sorted.
	low - (int) The starting index.
	high - (int) The ending index.
	'''

	if low < high: #Checking if the length of current list is at least 1.
		mid = int((low+high)/2)
		#Dividing the current list in two halves and sorting thmem:
		merge_sort(l,low,mid) 
		merge_sort(l,mid+1,high)
		#Merging the two slices of sorted lists: 
		merge(l, low, high, mid)

def merge(l, low, high, mid):
	'''
	This divides the list into two halves- left and right where the elements
	are already sorted, and then compares each element of the two lists to find
	the minimum and finally produce the sorted list.

	Arguments:
	l - (list) The list to be sorted.
	low - (int) The starting index.
	high - (int) The ending index.
	mid - (int) The position up to which the left and from where the right lists
	are to be sliced.
	'''
	left = l[low:mid+1] #Creating the left list.
	right = l[mid+1:high+1] #Creating the right list.
	print(f"Left list: {left}")
	print(f"Right list: {right}")

	#Appending a large number to deal with the lenghts of the lists.
	left.append(999999) 
	right.append(999999)

	i = j = 0

	#Making element-wise comparison and replacing values of the original list 
	  #with the minimum.   
	for index in range(low, high+1):
		if right[i] <= left[j]:
			l[index] = right[i]
			i += 1
		else:
			l[index] = left[j]
			j += 1
	print(f"Sorting and merging {left[:len(left)-1]} and {right[:len(right)-1]}")
	print(f"\t{l}\n")

if __name__ == '__main__':
	main()
