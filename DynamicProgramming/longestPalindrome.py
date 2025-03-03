# First approach: Brute-force method (inefficient for large inputs)
class Solution(object):
    def longestPalindrome(self, s):
        # Initialize the answer with the first character of the string
        answer = s[0]
        string_length = len(s)

        # Iterate through all possible substring lengths (starting from 2)
        for word_length in range(2, string_length + 1):
            # Iterate through all possible substrings of the given length
            for index in range(string_length - word_length + 1):
                word = s[index:index + word_length]  # Extract substring
                if check_palindrome(word):  # Check if it's a palindrome
                    answer = word  # Update answer if palindrome found
                index += 1  # Move to the next starting index
            word_length += 1  # Increment word length
        return answer  # Return the longest palindrome found

# Function to check if a string is a palindrome
def check_palindrome(word):
    length = len(word)
    
    # Single character is always a palindrome
    if length == 1: 
        return True
    elif length == 2:  
        first_half = word[0]  # First character
        latter_half_inverted = word[1]  # Second character
    
    # If the word length is even
    elif length % 2 == 0:
        j = (length - 2) / 2  # Middle index calculation
        first_half = word[:j+1]  # First half of the string
        latter_half = word[j+1:]  # Second half of the string
        latter_half_inverted = latter_half[::-1]  # Reverse second half
    
    # If the word length is odd
    elif length % 2 == 1:
        j = (length - 3) / 2  # Middle index calculation
        first_half = word[:j+1]  # First half of the string
        latter_half = word[j+2:]  # Second half of the string (excluding middle character)
        latter_half_inverted = latter_half[::-1]  # Reverse second half
    
    # Check if first half and reversed second half are the same
    if latter_half_inverted == first_half:
        return True


# Optimised approach: Expanding around center
class Solution(object):
    def longestPalindrome(self, s):
        longest_palindrome = s[0]  # Initialize with the first character
        
        # If string has only one character or is empty, return as is
        if len(s) == 1 or not s:
            return s
        
        # Iterate through each character in the string
        for i in range(len(s)):
            # Find the longest odd-length palindrome centered at index i
            odd_palindrome = check_left_right(s, i, i)
            
            # Find the longest even-length palindrome centered at index i, i+1
            even_palindrome = check_left_right(s, i, i + 1)

            # Update longest palindrome if a longer one is found
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome  # Return the longest palindrome found

# Helper function to expand around the center and find the longest palindrome
def check_left_right(s, left, right):
    # Expand as long as the characters on both sides are the same
    while left >= 0 and right < len(s):
        if s[left] != s[right]:  # Stop expanding if characters don't match
            break
        else:
            left -= 1  # Expand left
            right += 1  # Expand right
    
    # Return the longest palindrome found in this expansion
    return s[left+1:right]
