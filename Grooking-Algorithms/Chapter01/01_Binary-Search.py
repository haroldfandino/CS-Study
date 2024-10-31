orderedList = [2, 4, 6, 9, 15, 800]
def binary_search(orderedList, numberSearch):
    # Early check: If number is outside list range, return not found
    if numberSearch < orderedList[0] or numberSearch > orderedList[-1]:
        return "Not found"
    
    leftBoundary = 0
    rightBoundary = len(orderedList) - 1
    
    while leftBoundary <= rightBoundary:
        middle = (leftBoundary + rightBoundary) // 2
        
        if orderedList[middle] == numberSearch:
            return f"Found at index: {middle}"
        elif orderedList[middle] > numberSearch:
            rightBoundary = middle - 1
        else:  # if orderedList[middle] < numberSearch
            leftBoundary = middle + 1
    
    return "Not found"

# Get input and convert to integer
try:
    numberSearch = int(input("Enter a number to search: "))
    result = binary_search(orderedList, numberSearch)
    print(result)
except ValueError:
    print("Please enter a valid integer")