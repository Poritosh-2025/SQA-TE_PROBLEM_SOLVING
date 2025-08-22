def check_string(s):
    length = 0
    for char in s:
        length = length + 1
    if length<6 or length>15:
     return False

    for char in s:
        is_digit = False
        for digit in '0123456789':
            if char == digit:
                is_digit = True
                break
        
        is_letter = False
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if char == letter:
                is_letter = True
                break
    return True

        
value = str(input())
test_value = check_string(value)
print(test_value)