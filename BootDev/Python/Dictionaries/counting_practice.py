def count_enemies(enemy_names):
    
    enemies_dict = {}

    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1

    print(enemies_dict)
    
    return enemies_dict

enemy_01 = ["jackal", "kobold", "soldier", "jackal"]

count_enemies(enemy_01)

# Expected output.
# {"jackal": 2, "kobold": 1, "soldier": 1}