# Que.3)  Python program to replace the string space with a given character.

def replace_spaces(string, replacement_char):
    result = ''
    for ch in string:
        if ch == ' ':
            result += replacement_char
        else:
            result += ch
    return result


input_string = input("Enter String: ")
replacement_char = input("Character to Replace: ")

output = replace_spaces(input_string, replacement_char)
print("Updated string:", output)

# Output -
# Enter String: My name is Pradhi Bobade. 

# Character to Replace: _
# Updated string: My_name_is_Pradhi_Bobade._








