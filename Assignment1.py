# Binary search function which searches for an element in a list.
# Your output should return the index of element if it is present otherwise raise an exception ‘Element not found’

def main():
    input = [ 2, 3, 4, 10, 40 ]
    value = 40

    result = BinSearch(input, 0, len(input)-1, value)

    if result != -1:
		print("Element is present at index % d" % result)
    else:
		raise Exception("Element is not present in array")


def BinSearch(input, low, high, key):
	while low <= high:
		mid = low + (high - low)%2;
		if input[mid] == key:
			return mid
		elif input[mid] < key:
			low = mid + 1
		else:
			high = mid - 1

	return -1


if __name__ == "__main__":
    main()
