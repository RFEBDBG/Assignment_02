"""
#creating a list
list=[]
print("Blank list")
print(list)
print('1------------------------------------')

#creating a list of numbers
list1=[10,20,30,40,50]
print(list1)
print('1------------------------------------')

# creating a list of string 
list3=["Rahul","kumar","kamti"]
print(list3[0],list3[2])
print('1------------------------------------')

#creating a list of mixture data type
list4=[1,2,'Hello',3,4,'Rahul']
print(list4)
print('1------------------------------------')

# Geting the size of python list 
list4=[]
print(len(list4))
list5 =[1,2,3,4,4,5,5]
print(len(list5))
print(list5.count(4))
print('1------------------------------------')

# Accessing elements from list 
list6=['rahul','kumar','kamth']
print(list6[0],list6[2])
print('1------------------------------------')

# Accessing elemnts from multi-Dinmensional list 
list7=[['rahul','kamth'],['darbhanga']]
print(list7[0][1],list7[1][0])
print('1------------------------------------')

String= input("Enter element :")
lst=String.split()
print('list is ',lst)
print('1------------------------------------')

#  Using extend() method in python 
list8=[1,2,3,4,5]
print('initial string :')
print(list8)
# using extend method 
print("After extend list :")
list8.extend([6,'rahul','kamth'])
print(list8)
print('1------------------------------------')
# revers a list 
list9=[1,2,3,4,5,'kamth','kumar','rahul']
print(list9)
list9.reverse()
print(list9)
print(5 in list9)
print('1------------------------------------')
"""
square_num=[x**2 for x in range(10)]
print(square_num)


