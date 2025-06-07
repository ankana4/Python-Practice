# '''
#     *      (1, 2)
#   *   *    (1, 3)
# *   *   *  (1, 4)
# '''
# for i in range(2, 5):
#     for j in range(1, i):
#         print(" " +"*", end="")
#     print()    
    
    
x = [1, 2, 3, 4, 5]    #x=1,2,3,4,5
for i, n in enumerate(x): 
	if i == 2:
		break
	print(n) 
 
for i in range(2):   # i=0, 1
	for j in range(2): #j=0, 
		if j == 1:
			break
	print(i, j) 
print(i, j) 

# Create a list of 10 numbers (you may take user input)

list = []
for i in range(1, 11): 
    list.append(i)
print(list)  

#Calculate and print the sum of all numbers using a loop
sum = 0
for i in range(1, 11): 
    sum = sum+i
print(sum)  

#Find and print the largest number in the list using a loop

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list[0]
for i in list: #i=10
    if i > result: #10 > 9
        result = i  #result=10
print(result)   

#Create a new list containing only the even numbers from the original list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in list:
    if i % 2 == 0:
        new_list.append(i)
print(f"Even : {new_list}")


#Combine all questions 
list = []
sum = 0
for i in range(1, 11): 
    list.append(i)
    sum = sum + i 
print(list)
print(sum) 

result = list[0]
updated_list = []
for i in list:
    if i % 2 == 0:
        updated_list.append(i)
    if i > result:
        result=i
print(result)  
print(updated_list)  

#WAP that Creates a list of tuples, where each tuple contains a student name and their grade
#Uses a loop to print each student's information in the format: "Student: [name], Grade: [grade]"
#Finds and prints the name of the student with the highest grade
#Counts how many students have a grade above 80

list = []
for i in range(5):
    name = input("Enter name : ")
    grade = float(input("Enter grade : "))
    list.append((name, grade))
print(list)    

result = list[0]
for n in list:
    # print(f"Student : {n[0]}, Grade : {n[1]}") 
    if result[1] < n[1]:
    	result = n
print(result[0])

count = 0
for n in list:
    if n[1] > 80:
        count += 1
print(count)         
     
   