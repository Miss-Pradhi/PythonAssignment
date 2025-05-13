# Que. 6) Python program to count Occurrence Of Vowels & Consonants in a String.


def OccurrenceOfVowels_Consonants(original_string, ):
    vowelcount = 0
    ConsonantCount = 0
    
    for s in original_string:
        if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
            vowelcount = vowelcount + 1
        else:
            ConsonantCount = ConsonantCount + 1
  
    return vowelcount ,  ConsonantCount
    
    
original_string = input("Enter String: ")

result = OccurrenceOfVowels_Consonants(original_string, )
print (f"No. of vowels & consonants in given string is : {result} respectively")


# Output-

# Enter String: My name is Pradhi Bobade.
# No. of vowels & consonants in given string is : (8, 17) respectively