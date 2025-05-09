# Que.10) Write a program to accept 2 number and find greatest



P=int(input("Enter P: "))
Q=int(input("Enter Q: "))

if P<Q:
    print("Greater Value is : ", Q)
else:
    print("Greater Value is : ",P)

# =============================================================================


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