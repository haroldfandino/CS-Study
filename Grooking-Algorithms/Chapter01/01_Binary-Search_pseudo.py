"""
Array of ordered items.
Ask for number to search.
Check if array is empty - if empty, return "not found"

Set left boundary = 0
Set right boundary = length of array - 1

While left boundary <= right boundary:
    Calculate middle = (left + right) // 2
    If middle element == search number:
        Return "Found at index" + middle
    If middle element > search number:
        right boundary = middle - 1
    If middle element < search number:
        left boundary = middle + 1
Return "not found"
"""