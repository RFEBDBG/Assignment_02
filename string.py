# creating a string 
"""stirng1='welcome to python programming'
print(stirng1)

#creating a string in double Quotes
stirng2="welcome to python programming"
print(stirng2)

#creating a string in triple Quotes
stirng3='''i'm Rahul kumar dooing btech in computer science branch'''
print(stirng3)"""


# Accessing character in python string 
"""stirng1 ="welcome to python programming"
print(stirng1)

stirng2="welcome to python programming"
print("Last character of string ",stirng2[-1])"""

# string slicing in python
""""
string1="welcome to python programming"
print("initial string :",string1)
print(len(string1))

print("slicing character from 3-10")
print(string1[3:29])"""

# python string reverse 
"""string1="welcome to python pgogramming"
print(string1[::-1])
string2="".join(reversed(string1))
print(string2)"""


# Deleting or updating from string 
string1="I'm Rahul"
print("Initial stirng :",string1)
# As python string are immutable they don't support item updation directly
#There are 2 ways
#1
# list1=list(string1)
# list1[2]='ss'
# string12=''.join(list1)
# print("updating character at index 4 th position")
# print(list1)

# import keyword
# print(keyword.kwlist)

# neglact space 
# str1='  welcome to rahul   '
# print(str1)
# print(str1.strip())

# string join
strr=['rahul','kumar','kamth']
print(strr)
print("-".join(strr))

