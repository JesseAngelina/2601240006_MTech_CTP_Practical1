def binary_search(books, target):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2

        if books[mid] == target:
            return mid

        elif books[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Input
books = list(range(1, 1000001))
target = 75000

# Search
index = binary_search(books, target)

# Output
if index != -1:
    print("Book exists")
    print("Index =", index)
    print("Position =", index + 1)
else:
    print("Book does not exist")