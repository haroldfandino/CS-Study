level_test = 4

def calculate_experience_points(level):
    for i in range(level):

        current_level = i + 1

        next_xp = (i + 1) * 5

        if current_level == 1:
            current_xp = 0
        else:
            current_xp = (current_xp - 5) + next_xp

        print("Level " + str(current_level) + " XP for next level = " + str(next_xp) + " Current XP = " + str(current_xp))

calculate_experience_points(level_test)

level_test = 4

def calculate_experience_points(level):
    for i in range(level):

        current_level = i + 1

        next_xp = (i + 1) * 5

        if current_level == 1:
            current_xp = 0
        else:
            current_xp = (current_xp - 5) + next_xp

    return current_xp