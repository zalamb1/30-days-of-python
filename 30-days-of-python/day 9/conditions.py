#lvl1
#1
age=int(input("enter your age : "))
if age>=18:
    print("you are old enough to learn to drive")
else:
    n=18-age
    print("you need ",n," more years to learn to drive")
#2
x=int(input("Enter your age : "))
m=20
if x>m:
    if x-m ==1:
        print("you are 1 year older than me")
    else:
        print("you are ",x-m,"years oder than me")
elif m>x:
    if m-x==1:
        print('you are 1 year younger than me')
    else:
        print("you are ",m-x," years younger than me")
else:
    print("are you my twin???")
#3
a=int(input("give us a number"))
b=int(input("give us a second number"))
if a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)
#lvl2
# 1
s=int(input("give us your score on the test: "))
if s>=90 and s<=100:
    print("A")
elif s>=80 and s<=89:
    print("B")
elif s>=70 and s<=79:
    print("C")
elif s>=60 and s<=69:
    print("D")
else:
    print("F")
#2
month=input("Give us a month: ")
if month in["September","October","November"]:
    print("Autumn")
elif month in["December","January","February"]:
    print("Winter")
elif month in ["March","April","May"]:
    print("Spring")
elif month in ["June","July","Agust"]:
    print("Summer")
else:
    print("in what world you living?")
#3
fruite=print("Give us a fruite")
lst = ['banana', 'orange', 'mango', 'lemon']
if fruite in lst:
    print (lst)
else:
    lst.append(fruite)
    print(lst)