import time

def partition(array: list, low: int, high: int):
    """Function to find the partition position"""
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for the greater element
    i = low - 1
    
    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If an element smaller than pivot is found
            # Swap it with the greater element pointed by i
            i += 1
            # Swapping element at i with element at j
            array[i], array[j] = array[j], array[i]
    
    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]
    
    # Return the position from where partition is done
    return i + 1

def quickSort(array: list, low: int, high: int):
    """Function to perform quicksort"""
    if low < high:
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(array, low, high)
        
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

def main():
    array = map(int, input("Enter the numbers separated by ',' (comma): ").split(","))
    elements = list(array)
    print("Unsorted Array: ", elements)
    
    start = time.time()
    size = len(elements)
    quickSort(elements, 0, size - 1)
    end = time.time()
    
    print("Sorted Array:", elements)
    print("The time of execution of Deterministic Quick Sort is:",
          (end - start) * 10**3, "ms")

if __name__ == "__main__":
    main()
