# Que. 5) Python program to delete vowels in a given string.


def deleteVowels(original_string , vowelChars):
    
    result = ''
    for s in original_string:
        if s not in vowelChars:
            result = result+s
    return result
        
        
original_string = input("Enter String: ")
vowelChars = 'aeiou'

result = deleteVowels(original_string , vowelChars)
print("Updated String is : ", result)

# Output-
# Enter String: My name is Pradhi Bobade.
# Updated String is :  My nm s Prdh Bbd.
