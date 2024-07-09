## Arrays 101:
Arrays are a linear data structure, where the data is stored in contiguous memory location, and in most programming languages are used to store data of the same type.


### Basic Operations:
```python
# Create an array in python we use lists
arr = [] # Creating an array, in python arrays are dynamic so no need to specify the length

# Insert an element
arr.append("value") # append to the end O(1)
arr.insert(0, "value") # insert at the beginning O(N), not recommended, because this will shift all the values in the array to the right
arr.insert(index, "value") # insert at any index O(N), not recommended

# Delete an element:
arr.pop() # remove last item O(1)
arr.pop(0) # remove first item O(N), not recommended
arr.pop(index) # remove item at an index , not recommended
```
### Searching:
Linear Search: uses one pointer and we either iterate over the array forward or in reverse. O(N)
```python
# Forward:
for item in arr:
    do_something(item)

for i in range(0, len(arr)):
    do_something(arr[i])
step = 1
for i in range(0, len(arr), step):
    do_something(arr[i])
for idx, val in enumerate(arr):
    do_something(idx, val)
i = 0
while i < len(arr) - 1:
    do_something(arr[i])
    i += 1
# reverse:
step = -1
for i in range(len(arr) - 1, -1 , step):
    do_something(arr[i])
i = len(arr) - 1
while i >= 0:
    do_something(arr[i])
    i -= 1
```
Binary Search: usually applied on sorted arrays, where we compare the value we are looking for with the middle of the array, and based on that we check the right or left side of the array O(logN)

```python
def binary_search(arr, val):
    mid = len(arr) // 2
    if val == arr[mid]:
        do_somerthing(mid)
    elif val > arr[mid]:
        binary_search(arr[mid:], val) # search in the right side
    else:
        binary_search(arr[:mid], val) # search in the left side

```
### Techniques to improve efficiency:
Two Pointers: which can be initialized in two ways
1. opposite direction pointers: one start the the beginning and the other at the end
2. same direction pointers: both pointers start the the beginning and one could start slightly ahead of the other
Two pointers operate directly on the input data and doesn't require additional space. O(1)for extra space
Two pointers reduce time complexity from O(N^2) to O(N)
```python
def two_sum_sorted(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

def remove_duplicates(nums): # using in-place
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

def max_sum_subarray(nums, k): # sliding window
    max_sum = 0
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(1, len(nums) - k + 1):
        current_sum = current_sum - nums[i-1] + nums[i + k -1]
        max_sum = max(max_sum, current_sum)
    return max_sum
```
In-Place Operations: this method modify the input array, which means the original input will be lost, on the other hand it improves space complexity to O(1) of extra space.
```python
def quicksort(arr, low, high): # inplace
    if low < high:
        p1 = partition(arr, low, high)
        quicksort(arr, low, p1 - 1)
        quicksort (arr, p1+1, high)
        # notice the function doesn't use return because it applies changes on the array itself
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap
    arr[i+1], arr[high] = arr[high], arr[i+1] # swap pivot
    return i + 1
#######################
def reverse_arr(arr):
    left, right = 0, len(arr) - 1
    while left< righ:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
#######################
def remove_duplicate_sorted(nums):
    if not nums:
        return 0
    last_unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[last_unique_index]:
            last_unique_index += 1
            nums[last_unique_index] = nums[i]
    return last_unique_index + 1
#######################
def remove_duplicate_unsorted(nums):
    seen = set()
    write_index = 0
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.append(nums[i])
            nums[write_index] = nums[i]
            write_index += 1
    return write_index
```

[More python examples](arrays.py)