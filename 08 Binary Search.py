#Uncomment this function if using recursion. 
'''
def binarySearch(lst, key, high, low):
	if low <= high:
		mid = low + ((high - low) // 2)
		if lst[mid] == key:
			return mid
		elif lst[mid] < key:
			return binarySearch(lst, key, high, mid + 1)
		else:
			return binarySearch(lst, key, mid - 1, low)
	else:
		return None
'''

def main():
	l = input("Enter the numbers in your list\nsorted in ascending order\n(separated by spaces):\n").split()
	l = [int(item) for item in l]
	key = int(input("Enter key:"))

	high = len(l) - 1
	low = 0
	result = None

	#Comment from here...
	while low <= high and result == None:
		mid = low + ((high - low) // 2)
		if key == l[mid]:
			result = mid
		else:
			if key > l[mid]:
				low = mid + 1
			else:
				high = mid - 1
	#...to here if using recursion.

	#Use the below if using recursion:
	#reult = binarySearch(l, key, len(l) - 1, 0)
	
	if result == None: 
		print(f"{key} is not found.")
	else:
		print(f"{key} is found at index {result}.")

if __name__ == '__main__':
	main()