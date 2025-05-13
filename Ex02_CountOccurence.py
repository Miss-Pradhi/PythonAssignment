# Que.2) Python Program to count occurrence of a given characters in string.


input_string =  input("Enter String: ")
charTo_count = input("Character to Count: ")
occurrence_count = 0

for s in input_string:
    if s in charTo_count:
        occurrence_count = occurrence_count + 1

print ("Occurence of given Character is: ", occurrence_count)


# Output - 
# Enter String: My name is Pradhi Bobade. Currently pursuing Degree at Walchand College Of Enginnering, Sangli

# Character to Count: e
# Occurence of given Character is:  9

    
    
    
    