# Que.8) Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.


def FirstOccurrenceOfVowel(original_string, ):
    vowel = 'aeiouAEIOU'
    for s in original_string:
        if s in vowel:
            original_string = original_string.replace(s, '-', 1)
            break
        
    return original_string
        
    
original_string=input("Enter String: ")
result1 = FirstOccurrenceOfVowel(original_string, )
print ("Updated string is : ", result1)


# Output-
# Enter String: My name is Pradhi Bobade.
# Updated string is :  My n-me is Pradhi Bobade.
