# Que. 7) Python program to print the highest frequency character in a String.


s = input("Enter a string: ")

max_char = ''
max_count = 0

for char in s:
    count = s.count(char)
    if count > max_count:
        max_count = count
        max_char = char

print("Highest frequency character: ", max_char)
print("Frequency:", max_count)


# Output-
# Enter a string: Programmimg
# Highest frequency character:  m
# Frequency: 3
