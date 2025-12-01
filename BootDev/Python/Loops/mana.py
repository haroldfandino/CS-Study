mana = 0
max_mana = 10
num_potions = 9

def meditate(mana, max_mana, num_potions):
    while num_potions and mana < max_mana:
        num_potions -= 1
        print(f"num_potions = {num_potions}")
        mana += 1
        print(f"mana = {mana}")
    return mana, num_potions

meditate(mana, max_mana, num_potions)