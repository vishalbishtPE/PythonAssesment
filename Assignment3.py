#Given a new lexicographical order of alphabets, sort the list of strings according to the new order.

def main():
	order = "rcta" # Order in which we want teh string to be sorted
	inputArray = ["car", "rat", "cat",]  # Input Array which is already sorted according to alphabetical order
	lengthArray = len(inputArray)	# Length of Array

	sortStringArray(order, inputArray, lengthArray)


# Function to sort and print the array
# according to the new alphabetical order
def sortStringArray(order, inputArray, lengthArray):

	#Sort the array according to the new alphabetical order
	inputArray = sorted(inputArray, key = lambda word: [order.index(s) for s in word])

	print(inputArray)


if __name__ == "__main__":
	main()
