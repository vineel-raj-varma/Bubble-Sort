def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			if arr[i] < arr[j]:
				arr[i], arr[j] = arr[j], arr[i]
	print(arr)					


arr = [5,9,6,5,8,6,2,8,5,4,2,3,0]

bubble_sort(arr)

# If input is [5, 9, 6, 5, 8, 6, 2, 8, 5, 4, 2, 3, 0]
# Output will be [0, 2, 2, 3, 4, 5, 5, 5, 6, 6, 8, 8, 9]

