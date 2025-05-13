# Que.1) Python program to remove given character from String.
      
        
# Function to remove a given character from a string
def remove_character(string, char_to_remove):
    return string.replace(char_to_remove, '')

input_string = input("Enter String: ")
char_to_remove = input("Enter Character to remove: ")

result = remove_character(input_string, char_to_remove)
print("Character to remove:", char_to_remove)
print("Updated string:", result)



# Output -

# Enter String: My name is Pradhi Bobade. Currently pursuing Degree at Walchand College Of Enginnering, Sangli

# Enter Character to remove: e
# Character to remove: e
# Updated string: My nam is Pradhi Bobad. Currnt pursuing Dgr at Walchand Collg Of Enginnring, Sangli