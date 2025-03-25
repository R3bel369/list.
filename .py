#Create a list of integers from 1 to 10.
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)
#How can you access the first element of a list?

a=[5,6,7,8,9,10]
print(a[0:1])

#Write a Python code to append an element to the end of a list.
k=['a','b','c']
k.append('d')
print(k)

#How do you remove the last element from a list?
c=[6,7,8,9,10]
c.pop(-1)
print(c)

#How can you find the length of a list?
d=[1,2,3,4,5,6,7,8]
print(len(d))

#Write a Python program to find the largest number in a list.
d=[1,2,3,4,5,6,7,8,10]
print(max(d))

#How can you sort a list in ascending order?
a=['a','b','A','B']
a.sort()
print(a)

#Write a code to check if an element is present in a list or not.
a=[1,2,3,4,5]
a=[i for i in a if i==5] 
print(a)
#How do you find the index of an element in a list?
a=[5,9,8,4,6]
print(a[0])## (list.index value of the element)
#How can you create a list of 5 elements, then remove all of them?
a=[2,5,8,9,1,5]
print(a.clear())
#How can you slice a list to get elements from index 2 to 5?
p=[1,3,5,7,9,11,13,15]
print(p[2:6])
#How can you concatenate two lists in Python?
a=[1,2]
b=[3,4]
a.extend(b)
print(a)
#How can you copy a list into another list?
a=[2,4,6,8]
b=a.copy()
print(b)

#Write a Python program to count the number of times an element appears in a list.
a=[1,3,3,7,9]
c=0
for i in a:
    if i==3:
        c+=1
print(c)
#How can you check if a list is empty?
a=[2]
if a==[]:
    print('Empty list')
else:
    print('Not empty list')  
#String Questions:
#Create a string variable that holds your name and print it.
a='shiva'
print(a)

#How do you convert a string to uppercase in Python?
a='shiva'
print(a.upper())
#Write a code to check if a string contains a specific substring.
a='abcd'
for i in a:
 if i in 'cd':
    print(i,'it is part of given string')
#How can you find the length of a string in Python?
a='abcdefgh'
print(len(a))
#Write a Python program to reverse a string. 
a='MOMDAD'
print(a[::-1])

