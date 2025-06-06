my_dict = {'model' : 'iPhone', 'reference' : 11}
my_dict['batery_life'] = 83

print(my_dict)

# Methods

list(my_dict.keys())
list(my_dict.values())
my_dict.get('models')

## Update

my_dict_new = {'color' : 0x000000, 'reference' : 16}
my_dict.update(my_dict_new)
print(my_dict)

## Pop

my_dict.pop('color')
print(my_dict)

## Convert to a list

my_list = list(my_dict.keys())
print(my_list)

print(my_list[0])

# Alternative

my_dict_2 = dict(size = 'large', color = 0xfffffff)
print(my_dict_2)
