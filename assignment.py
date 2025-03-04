#Assignment
#Numeric datatypes
#integers
num3 = 2
print(num3, 'is of type',type(num3))

num2 = 9.1
print(num2,'is of type',type(num2))

num4 = 1+2j
print(num4,type(num4))   


# strings
colours=' I love red with blue'
print(colours)


#List datatype
Fruits=["apples", "bananas", "oranges"]
print(Fruits)
students_detail ={"name":"Ejidia","track":"python","gender":"Female","age":21}
print(students_detail["name"])
print(students_detail.keys())
print(students_detail.values())

# set datatype
student_id={20, 30, 35, 40,2 ,30 ,40}
print (student_id)


#Indented lists
good=[10,[30,48,20,[100,[49,80,[21]]]]]
print(good[1][3][1][2][0])

num =[1,3,[3,[7,"hello"]]]
print(num[2][1][1])

#OPERATORS
num= 2
num1= 3
#addition
print(num + num1)
print(num + num1)
# subtraction
print(num - num1)
print(num * num1)
print(num / num1)
print(num // num1)
print(num ** num1)
print(num % num1)
print(num % num1)


#assignment operators
num3 = 10
num3 += 10
num3 -= 10 
print(num3)
num3 -= 10
print(num3)
num *= 10
print(num3)
num**= 10
print(num3)


num1= int(input("input your first number"))
num2= int(input("input your second number"))
operator=input("choose the operator")
print(num1,operator,num2)
if num1 >=num2:
   print(num1>=num2)
if num1%num2 ==0:
   print(num1% num2 ==0)
   print(f"{num1} is divisible by{num2}")
if num1 is not 0:
   num2 += num1
   print(num2)
#These compare two values and a boolean
num1 =20
num3 =30
#is less than#is less than
print(num3 >num1) 
#is greater than
print(num1 >num3) 
# greater than or equal to
print(num3 >=num1)
#less than or equal to
print(num1 <=num3)
# not equal to
print(num1 !=num3)
# false
print(num1 ==num3)

# Logical operators
#and(&), or(||), not(!)
log1 =5
log2 =6

print((log1 >log2) and (log2<log1))
print( not (log2<log1))
print((log1 >log2) or(log2<log1))
print(True and True)
print(True and False)
print(not True)
print(True or True)
print(True or False)
print(False or False)

#Membership operators
members= [20,30,40,50]
print( 20 in members)
print(20 not in members)

name="Ejidia"
print("e" not in name)
print("E" not in name)


#Identity operators
print(20 is not members)
print(20 is 20)


