#Conditional Statements - if else
#check whether the given number is Even or Odd
'''
x = int(input("Enter no:"))
if x%2==0:
    print("Even")
else:
    print("Odd")
'''
#Single Line If else
'''
x = int(input("Enter no:"))
print("Even" if x%2==0 else "Odd")
'''
#find the largest b/w 2 two number
'''
x = int(input("Enter No1 :"))
y = int(input("Enter No2 :"))
if x>y:
    print(x, " is largest")
elif x==y:
    print("Both are equal")
else:
    print(y, " is largest")
'''
#you have 3 sides , if they are able to form a traingle,which
#traingle is it?
#Equilateral(all sides are equal) / Isoceles(any two) / Scalene
x = int(input("Enter Side1 :"))
y = int(input("Enter Side2 :"))
z = int(input("Enter Side3 :"))

if x+y>z and y+z>x and z+x>y:
    if x==y and y==z:
        print("Equilateral Traingle")
    elif x==y or y==z or z==x:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Traingle is invalid")
    
