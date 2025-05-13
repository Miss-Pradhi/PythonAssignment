# Ques.4)  Python program to replace the string space with a given character using replace() method.


def replaceSpace(original_string , replacible_Char):
    return original_string.replace(" " , replacible_Char)
    

original_string = input("Enter String: ")
replacible_Char = input("Character to Replace: ")

result = replaceSpace(original_string , replacible_Char)
    
print ("Updated String is: ", result)


# Output-
# Enter String: My name is Pradhi Bobade. Currently pursuing Degree at Walchand College Of Enginnering, Sangli

# Character to Replace: _
# Updated String is:  My_name_is_Pradhi_Bobade._Currently_pursuing_Degree_at_Walchand_College_Of_Enginnering,_Sangli
