#Que.1) Addition of two numbers
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
addition = a+b
print("Addition is : ", addition)
#--------------------------------------------------------------



#Que.2) Perform all arithmatic
a =10 #Assign value 10 to the variable a
print (a)   #a=10

a+=10 #a=a+10 --> 10+10=20
print(a) #a=20

a*=2    #a=a*2 --> a=20*2=40
print(a)    #a=40

a/=5    #a=a/5 --> a=8.0
print(a)    #a=8.0

a//=5
print('floor division :',a) 
#--------------------------------------------------------------



#Que.3) find the Area Rectangle
length=int(input("Enter length : "))
breadth=int(input("Enter breadth : "))
area = length*breadth
print("Area of rectanlge = ", area)
#--------------------------------------------------------------



#Que.4) Find the Area of Triangle
base=int(input("Enter Base : "))
height=int(input("Enter Height : "))
area = 1/2*base*height
print("Area of Triangle = ", area)
#--------------------------------------------------------------



#Que.5) Square of the number
a=int(input("Enter the number: "))
square=a*a
print("Square of given Number is : ", square)
#--------------------------------------------------------------



#Que.6) Cube of the number
a=int(input("Enter the number: "))
cube=a*a*a
print("Cube of given Number is : ", cube)
#--------------------------------------------------------------



#Que.7) Calculate total Average
Marathi=int(input("Enter the Marks of Marathi: "))
Maths=int(input("Enter the Marks of Matha: "))
Science=int(input("Enter the Marks of Science: "))
English=int(input("Enter the Marks of English: "))
Geography=int(input("Enter the Marks of Geography: "))

total = Marathi+Maths+Science+English+Geography
Average = (Marathi+Maths+Science+English+Geography)/5
percentage = (total/500)*100
print("Total marks in 5 subject is : ", total)
print("Total Average of marks in 5 subject is : ", Average)
print("Percentage of marks in 5 subject is : ", percentage)
#--------------------------------------------------------------



# Que.8) Calculate simple interest
P=int(input("Enter P: "))
R=int(input("Enter Q: "))
T=int(input("Enter T: "))
SimpleInterest=(P*R*T)/100
print("Simple Intrest is: ",SimpleInterest)
#--------------------------------------------------------------


# Que.9) Swap values of two integer variables 
P=int(input("Enter P: "))
Q=int(input("Enter Q: "))
temp = P
P=Q
Q=temp
print("Value of P: ",P)
print("Value of Q: ",Q)
#--------------------------------------------------------------



# Que.10) Write a program to accept 2 number and find greatest
P=int(input("Enter P: "))
Q=int(input("Enter Q: "))

if P<Q:
    print("Greater Value is : ", Q)
else:
    print("Greater Value is : ",P)
#--------------------------------------------------------------



# Que.11) WAP to accept 3 numbers & print the greatest
P=int(input("Enter P: "))
Q=int(input("Enter Q: "))
T=int(input("Enter T: "))

if P<Q:
    print("Greater Value is : ",Q)
elif Q<T:
    print("Greater Value is : ",T)
else:
    print("Greater Value is : ",P)
