# O(N) Time Complexity | O(1) Space Complexity
def isMonotonic(array):
    isIncreasing = True  # Assume Both True first
    isDecreasing = True

    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            isDecreasing = False  # If increasing it cant be decreasing
        if array[i] > array[i + 1]:
            isIncreasing = False  # If decreasing it cant be increasing

    # If either is true then the array is monotonic
    return isIncreasing or isDecreasing
