def main():
	l = input("Enter the numbers in your list (separated by spaces):\n").split()
	l = [int(item) for item in l]
	key = int(input("Enter key:"))
	flag = False

	for i in range(len(l)):
		if l[i] == key:
			flag = True
			break
	
	if flag:
		print(f"{key} found. First occurance at index {i}.")
	else:
		print(f"{key} not found in list.")

if __name__ == '__main__':
	main()
