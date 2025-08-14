def position_of_pattern(text, pattern):
    
    print(f"Text is: {text} && Pattern is: {pattern}")
    positions = []
    a = len(text)
    b = len(pattern)
    print(f"Text length of : {a}, pattern length of: {b}")

    for i in range(a - b +1):
        if text[i:i+b] == pattern:
            print(f"{text[i:i+b]}")
            positions.append(i)
    return positions

text = str(input())
pattern = str(input())
positions = position_of_pattern(text, pattern)
print("Pattern found of position:", positions)