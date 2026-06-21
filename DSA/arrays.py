from array import *
# In Python these type of arrays contains selective type of elements only


# a = array(typecode, [...element])  | other ways of using  a = array.array()



# ====== typecode ======
# b, h -> signed integer
# B, H -> unsigned integer

# u -> unicode character

a1 = array('i', [1,2,3,4,56,99,10000])
print(type(a1))
print(a1)

for x in a1:
    print(x, end=' ')

print('\n')

for i in range(3):
    print(a1[i], end=' ')

a1[3] = 75
print(a1)
print('\n')

# list (contains any type of element)
l = [2, 3, 'a', 'b', 55, "hello"]
for ele in l:
    print(ele, end=', ')
