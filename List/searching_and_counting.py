#First occurrence
#Find the index of the first 7.
numbers = [4, 7, 2, 7, 9]
for i in range(len(numbers)):
    if numbers[i] == 7:
        print(i)
        break
    

#Last occurrence
#Find the index of the last 7 without using a reverse-index shortcut.    
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] == 7:
        print(i)
        break