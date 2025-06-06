# Create dictionary using zip

my_dict = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
#print(my_dict)

# Now, using a comprehension

my_dict2 = {x : x**2 for x in [1, 2, 3]}
# print(my_dict2)

my_list = ['a', 'b', 'c']
my_dict3 = {i : i*2 for i in my_list}
print(my_dict3)