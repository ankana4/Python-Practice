#Group numbers into even and odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
temp_dict = {
    "even":[],
    "odd": []
}
for num in numbers:
    if num % 2 == 0:
        temp_dict["even"].append(num)
    else:
        temp_dict["odd"].append(num)
print(temp_dict)            