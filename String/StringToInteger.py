def myAtoi(s):
    #remove any leading whitespace
    s = s.lstrip()

    #Initialize result string as "0" in case no digits were found
    s_return = "0"

    #If the string is empty after stripping return zero
    if s == "":
        return 0
    
    #If the first character is "-" output a negative number
    if s[0] == "-":
        for char in s[1:]:   #start iterating from the second character
            if char.isdigit():   #check whether character is a digit
                s_return += char   #append the character to return string if its a digit
            else:
                break  #Stop processing if a non-digit character is found
        output = 0 - int(s_return) #Convert to integer and make it negative
        
    #If the first character is "+" output a positive number        
    elif s[0] == "+":
        for char in s[1:]:
            if char.isdigit():
                s_return += char
            else:
                break
        output = int(s_return)

    #If no sign is present process the string as usual
    else:
        for char in s: #Here we iterate from the start
            if char.isdigit():
                s_return += char
            else:
                break
        output = int(s_return)

    #Clamp the output within 32-bit integer range
    if output > (2**31)-1:
        output = 2**31 - 1
    elif output < -(2**31):
        output = -2**31
    
    return output  #Return the final integer