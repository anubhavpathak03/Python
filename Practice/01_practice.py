#  list
nums = [3, 0, 1, 4] 

for i, v in enumerate(nums):
    print(i, v)

print();

for index, num in enumerate(nums):
    print(f"Index {index} => {num} ");


print(list(enumerate(nums)));