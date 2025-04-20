# define a dictionary and add values to it
my_dict = {'apple': 3, 'banana': 2, 'orange': 4, 'grapes': 1}

# define a function to find the key-value pair with the maximum value
def my_max(dict):
    max_value = None
    max_pair = None
    for key, value in dict.items():
        if max_value is None or value > max_value:
            max_value = value
            max_pair = (key, value)
    return max_pair

# define a function to find the key-value pair with the minimum value
def my_min(dict):
    min_value = None
    min_pair = None
    for key, value in dict.items():
        if min_value is None or value < min_value:
            min_value = value
            min_pair = (key, value)
    return min_pair

# test the functions
print('The maximum key-value pair is:', my_max(my_dict))
print('The minimum key-value pair is:', my_min(my_dict))
