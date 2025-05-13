# Que.9)  Python program to count alphabets, digits and special characters.

def countAlphabetsDigitsSpecialChar(original_String, ):
    alphaCount = 0
    digitCount = 0
    specialCharCount = 0
    
    for s in original_String:
        if s.isalpha():
            alphaCount = alphaCount + 1
        elif s.isdigit():
            digitCount = digitCount + 1
        else:
            specialCharCount = specialCharCount + 1
    return alphaCount, digitCount, specialCharCount
  

original_String = input("Enter String: ")
x,y,z = countAlphabetsDigitsSpecialChar(original_String, )
print ("Alphabets Count is : ", x)
print ("Digit Count is : ", y)
print ("Special Character Count is : ", z)

# Output - 
# Enter String: My email ID is bobadepradhi3008@gmail.com
# Alphabets Count is :  31
# Digit Count is :  4
# Special Character Count is :  6

