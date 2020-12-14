not_weird_nums = list(range(22, 101, 2))
not_weird_nums.append(2)
not_weird_nums.append(4)
print(not_weird_nums)

n = int(input("What is n? "))
if n in not_weird_nums:
    print("Not Weird")
else:
    print("Weird")

# solution code ended up a little different:
not_weird_nums = list(range(22, 101, 2))
not_weird_nums.append(2)
not_weird_nums.append(4)
# print(not_weird_nums)

n = int(input())
if n in not_weird_nums:
    print("Not Weird")
else:
    print("Weird")
