def heapify(nums_arr, heap_size, root_index):
    largest_number = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums_arr[left_child] > nums_arr[largest_number]:
        largest_number = left_child
    if right_child < heap_size and nums_arr[right_child] > nums_arr[largest_number]:
        largest_number = right_child
    if largest_number != root_index:
        nums_arr[root_index], nums_arr[largest_number] = nums_arr[largest_number], nums_arr[root_index]
        heapify(nums_arr, heap_size, largest_number)

def heap_sort(nums_arr):
    n = len(nums_arr)
    for i in range(n, -1, -1):
        heapify(nums_arr, n, i)
    for i in range(n - 1, 0, -1):
        nums_arr[i], nums_arr[0] = nums_arr[0], nums_arr[i]
        heapify(nums_arr, i, 0)

nums = [0, 9, 7, 5, 3, 8, 6, 2, 4, 1]
heap_sort(nums)
print(nums)