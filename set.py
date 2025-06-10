'''
Set is build-in data type in Python
It is used to store unordered, unindexed and unique elements.
Set automatically removes duplicate data
It is mutable(add or remove)
Cannot store multiple types data like list, and dictionary inside a set
'''

#Creating a set
my_set = {1, 2, 3}
print(my_set)

another_set = set([3, 4, 5])
print(another_set)

#Basic set operations
A = {1, 2, 3}
B = {3, 4, 5}

#Union
print(A | B)

#Intersection
print(A & B)

#Difference
print(A - B)

#Modifying set
s = {1, 2}
s.add(3)
s.remove(3)
s.discard(10)
s.update([4, 5])
print(s)

#Removing duplicates from a list
emails = ['a@x.com', 'b@x.com', 'a@x.com']
unique_emails = set(emails)
print(unique_emails)

#Membership tetsing
blaclist = {'1234', '5678'}
card = '1234'
if card in blaclist:
    print('Card is blocked')

#Find common customers between two sources
site_users = {'Alice', 'bob', 'Charlie'}
app_users = {'bob', 'David', 'Alice'}

common_users = (site_users & app_users)
print(common_users)

#Logging unique ip address
unique_ip = set()

def log_ip(ip):
    if ip not in unique_ip:
        unique_ip.add(ip)
        print(f'new visitor : {ip}')
        
log_ip('192.168.1.1')
log_ip('192.168.1.2')
log_ip('192.168.1.1')        


#User input to create a set

my_set = set()
for i in range(1, 3):
    data = input("Enter a set value : ")
    my_set.add(data)
print(my_set)    