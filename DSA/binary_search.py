"""
Two-way to implement the binary search algorithm.
1. iterative binary search algorithm
2. Recursive binary search algorithm
"""


def iterative_binary_search(array: list, search_element: int) -> str:
    """Search the search element in the given sorted array in iterative manner."""
    low, high = 0, len(array) - 1
    mid = low + (high - low)//2

    print(f"Low:{low}, mid:{mid}, high:{high}")
    while low <= high:
        if search_element == array[mid]:
            return f"Search element {search_element} found in position {mid}"
        elif search_element < array[mid]:
            high = mid - 1
            mid = low + (high - low) // 2
            print(f"Low:{low}, mid:{mid}, high:{high}")
        elif search_element > array[mid]:
            low = mid + 1
            mid = low + (high - low) // 2
            print(f"Low:{low}, mid:{mid}, high:{high}")
    return f"Search element:{search_element} not found in the array"


def recursive_binary_search(array: list, low_idx: int, high_idx: int, query: int) -> str:
    if high_idx > low_idx:
        mid = low_idx + (high_idx - low_idx) // 2
        if array[mid] == query:
            return f"search element {query} found in the position {mid}"

        elif array[mid] > query:
            return recursive_binary_search(array, low_idx, mid -1, query)
        elif array[mid] < query:
            return recursive_binary_search(array, mid + 1, high_idx, query)

    return f"Search element:{query} not found in the array"


input1 = [8, 9, 20, 25, 66, 90, 100]
search = 90
#print(iterative_binary_search(input1, search))
print(recursive_binary_search(input1, 0, len(input1)-1, search))
