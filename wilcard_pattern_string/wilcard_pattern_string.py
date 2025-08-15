def find_wilcard_pattern(text, pattern):
    words = text.split()
    print(f"{words}")
    prefix = pattern.split('*')[0]
    suffix = pattern.split('*')[1]
    print(f"prefix is: {prefix} and suffix is: {suffix}")

    matches = []
    for word in words:
        if word.startswith(prefix) and word.endswith(suffix):
            if len(word) >= len(prefix) + len(suffix):
                matches.append(word)
    return matches 

text = "A laxy brown fox jumps lasdjy over the lazy dog"
pattern = "la*y"
result = find_wilcard_pattern(text, pattern)
print(f"Final result is: {result}")