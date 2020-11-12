# Task 1
# Declare a list with numbers 1 to 5 and add 6 at the end of the list
nlist = [1, 2, 3, 4, 5]
nlist.append(6)
print(nlist)

print("*"*30)
# Task 2
# Create a tuple with values 1 to 5 then iterate through and rint until 3 then stop
nums = {1, 2, 3, 4, 5}

for _ in nums:
    if _ > 3:
        break
    print(_)

