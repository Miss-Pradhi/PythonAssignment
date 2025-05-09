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