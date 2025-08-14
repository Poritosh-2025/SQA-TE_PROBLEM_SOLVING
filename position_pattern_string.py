def find_pattern_positions(text, pattern):
    """
    Finds all starting positions of a given pattern within a string.
    
    Args:
        text (str): The string to search within.
        pattern (str): The pattern to search for.

    Returns:
        list: A list of integers representing the starting indices
              where the pattern is found. Returns an empty list if
              the pattern is not found.
    """
    positions = []  # Initialize an empty list to store the positions
    n = len(text)   # Calculate the length of the text
    m = len(pattern) # Calculate the length of the pattern
    
    # Debugging: print lengths of text and pattern
    print(f"Text length: {n}, Pattern length: {m}")
    
    if m == 0:  # If the pattern is empty, return all positions
        # Debugging: print when the pattern is empty
        print("Pattern is empty. Returning all positions.")
        return list(range(n + 1))

    # Iterate through the text to find matches
    for i in range(n - m + 1):  # Loop from the start to where the pattern could fit
        # Debugging: show current index and the slice of text being compared
        print(f"Checking position {i}: text[{i}:{i + m}] = '{text[i:i + m]}'")
        
        if text[i:i + m] == pattern:  # Check if the current slice matches the pattern
            
            # If it matches, append the starting index to positions list
            positions.append(i)
            # Debugging: print when a match is found
            print(f"Match found at index {i}")
            
    # Debugging: print the final positions list
    print(f"Final list of positions: {positions}")
    return positions

# Example usage
text = "This is a test string, and this is another test."
pattern = "test"

# Call the function with debug prints enabled
positions = find_pattern_positions(text, pattern)
print("Pattern found at positions:", positions)