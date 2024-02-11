import random
import time
numberRange = 1000
numberCount = 500


numbers = []


for i in range(numberCount):#Generate some random numbers to test on
    numbers.append(random.randint(0,numberRange))

print("Unsorted numbers: ", numbers)

def bubbleSort(array):
    start = time.time()
    n = len(array)
    swapped = False
    for i in range(n-1):#loop through all numbers
        for j in range(n-i-1):#n numbers where i numbers are already sorted
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
    end = time.time()
    print(end - start)
    return array


print("Sorted numbers:   ", bubbleSort(numbers))