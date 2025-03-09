def isPalindrome(x):
    #Convert Integer into a String
    x_str = str(x)

    #Inverted String
    x_inverted = x_str[::-1]

    #Compare Original and Inverted String
    if x_str == x_inverted:
        return True
    else:
        return False
    

#Without converting to a string
def isPalindrome2(x):
    #negative numbers are not palindromes and numbers ending in zero are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False 
    
    #One digit numbers are palindromes
    if x>0 and x<10:
        return True
    
    #reverse half of the number
    reversed_half = 0

    while x > reversed_half :
        reversed_half = reversed_half * 10 + x % 10  #Extract the last digit from x and add it to reversed half
        x = x // 10  #remove last digit from x

    return x == reversed_half or x == reversed_half // 10  #Two cases due to odd and even number of digits