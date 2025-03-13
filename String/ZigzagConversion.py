def convert(s, numRows):
    # If numRows is 1 or string length is greater than 1000, return the string as it is
    if numRows == 1 or len(s) > 1000:
        return s
    
    # Create an empty list for each row in the zigzag pattern
    zigzag_array = [[] for i in range(numRows)]

    index = 0  # Keeps track of the current row
    direction = 1  # Determines the direction of movement (down = 1, up = -1)

    # Iterate over each character in the string
    for char in s:
        zigzag_array[index].append(char)  # Append character to the corresponding row
        
        # Change direction at the top and bottom of the zigzag pattern
        if index == 0:
            direction = 1  # Move down
        elif index == numRows - 1:
            direction = -1  # Move up
        
        index += direction  # Update row index based on direction

    # Convert each row list into a string
    for j in range(numRows):
        zigzag_array[j] = "".join(zigzag_array[j])
    
    # Join all rows to form the final zigzag-converted string
    return "".join(zigzag_array)
