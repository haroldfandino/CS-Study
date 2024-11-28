number_s = 4
number_l = [1, 2, 3, 4, 50]

def linear_search(number_search, number_list):
    for index, value in enumerate(number_list):  # Use enumerate to get both index and value
        if value == number_search:
            print(f"Found at index {index}")
            return index  # Return the index when the number is found
    print("Not found")
    return -1  # Return -1 if the number is not found

linear_search(number_s, number_l)