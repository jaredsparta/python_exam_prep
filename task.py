# Task 1
# Declare a list with numbers 1 to 5 and add 6 at the end of the list
nlist = [1, 2, 3, 4, 5]
nlist.append(6)
print(nlist)

print("*"*30)
# Task 2
# Create a tuple with values 1 to 5 then iterate through and print until 3 then stop
nums = {1, 2, 3, 4, 5}

for _ in nums:
    if _ > 3:
        break
    print(_)

print("*"*30)
# Task 3
# Declare a shopping list dictionary
shop_dict = {1:"bread", 2:"bananas", 3:"apples"}
for key, value in shop_dict.items():
    print(f"{key} : {value}")
    print(type(value))