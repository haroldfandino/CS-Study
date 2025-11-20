# Skip every 7 number

# counter = 0
# for number in range(1, 51):
#     counter = counter + 1

#     if counter == 7:
#         counter = 0 # Reset the counter
#         continue # Skip this number

#     print(number)

# Skip negative numbers

# numbers = [16, -4, 25, -9, 36, 0, 49]

# for number in numbers:
#     if number < 0:
#         continue  # Skip negatives to avoid complex numbers

#     print(f"The square root of {number} is {number ** 0.5}.")

# Enchantment assessment

def award_enchantments(start, end, step):

    counter = 0

    for quest_number in range(start, end, step):
        
        counter = counter + 1

        if counter < 3:
            continue

        counter = 0

        enchantment_strength = quest_number * 5
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )

award_enchantments(1, 11, 1)

