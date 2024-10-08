import random
import time

def quicksort_randomized(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]
    
    return quicksort_randomized(less) + [pivot] + quicksort_randomized(greater)

def measure_sort_performance(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr[:])
    end_time = time.time()
    return sorted_arr, end_time - start_time

if __name__ == "__main__":
    array_size = 20  
    test_array = [random.randint(0, 100) for _ in range(array_size)]
   
    print(f"Unsorted Array:\n{test_array}")
    
    sorted_randomized, time_randomized = measure_sort_performance(quicksort_randomized, test_array)
    
    # Print sorted array for randomized quick sort
    print(f"\nRandomized Quick Sort:")
    print(f"Sorted Array:\n{sorted_randomized}")
    print(f"Time: {time_randomized:.6f} seconds")
