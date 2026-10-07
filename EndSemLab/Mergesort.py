def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, c1 = merge_sort(arr[:mid])
    right, c2 = merge_sort(arr[mid:])

    result = []
    i = j = 0
    comparisons = c1 + c2

    while i < len(left) and j < len(right):
        comparisons += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, comparisons


# Test cases
sorted_input = [10, 15, 20, 25, 30, 35, 40]
reverse_input = [40, 35, 30, 25, 20, 15, 10]
random_input = [25, 10, 40, 15, 30, 20, 35]

for name, arr in [
    ("Already Sorted", sorted_input),
    ("Reverse Sorted", reverse_input),
    ("Random", random_input)
]:
    result, comparisons = merge_sort(arr)

    print("\n", name)
    print("Input:", arr)
    print("Sorted:", result)
    print("Comparisons:", comparisons)