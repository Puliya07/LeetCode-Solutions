def myAtoi(s):
    #remove leading whitespace
    s = s.lstrip()

    if not s:
        return 0 #return 0 if s is empty
    
    sign = 1 #default sign
    index = 0 #default index
    output = 0 #initial condition

    if s[0] in ['-', '+']: #if the sign is mentioned
        if s[0] == '-':
            sign = -1 #change the sign if '-' is given in front
        index += 1 #increment the current index

    while index < len(s) and s[index].isdigit(): #Iterate through the string while checking the character is a digit
        output = output * 10 + int(s[index])   # construct the integer
        index += 1

    output *= sign  #include correct sign

    MIN, MAX = -2**31-1 , 2**31  #declaring min and max according to 32-bit integer range

    return max(min(output, MAX), MIN)