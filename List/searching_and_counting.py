#First occurrence
#Find the index of the first 7.
numbers = [4, 2, 2, 7, 9]
for i in range(len(numbers)):
    if numbers[i] == 7:
        print(i)
        break