from first_line import fun

fun("carrot")
fun("anubhav")

print('\n')

squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_nums = [y**3 for y in range(5)]
print(cube_nums) 


print('\n')

dict = {
    "name": "insaan", 
    "age": "nhi pata", 
    "work": "Soldier", 
    "region": "Bharat"
}

for people in dict:
    print(people, "-> ", dict[people])

print('\n')

for key, values in dict.items():
    print(key, "=> ", values)

print('\n')


for key in dict.keys():
    print(key)


print('\n')

tea_shope = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"},
}
print('\n')
print(tea_shope)
print('\n')
print(tea_shope["chai"])
print('\n')
print("""tea_shope["Tea"]["Green"] => """, tea_shope["Tea"]["Green"])


print('\n')
new_squared_nums = {x: x**2 for x in range(10)}
print(new_squared_nums)


print('\n')
keys = ["Masala", "Spicy", "Lemon"]
default_values = "Delicious"

new_dict = dict.fromkeys(keys, default_values)
print(new_dict)
print('\n')


# tuples
tea_types = ("Masala", "Ginger", "Oolong") 
print(tea_types)

left_tea_types = ("Lemon", "Green", "0-Suger")

all_tea_types = tea_types + left_tea_types
print(all_tea_types)

print('\n')
person = ("Anubhav", 22, "Cricket, Chess, Tenis")

(name, age, Hobbies) = person

print(name) # "Anubhav"
print(age)
print(Hobbies)



print('\n')



# iterables tools 



f = open('first_line.py')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline())