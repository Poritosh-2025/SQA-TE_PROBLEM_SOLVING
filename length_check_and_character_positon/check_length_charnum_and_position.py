def check_password(password):
    length = 0
    for char in password:
        length = length+1
    if length<8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    digit_chars = '0123456789'

    for char in password:
        if not has_uppercase:
            for uc in uppercase_chars:
                if char == uc:
                    has_uppercase = True
                    break 

        if not has_lowercase:
            for lc in lowercase_chars:
                if char == lc:
                    has_lowercase = True
                    break

        if not has_digit:
            for dc in digit_chars:
                if char == dc:
                    has_digit = True
                    break

        if not has_special:
            is_letter_or_digit = False

            for uc in uppercase_chars:
                if char == uc:
                    is_letter_or_digit = True
                    break
            if not is_letter_or_digit:
                for lc in lowercase_chars:
                    if char == lc:
                        is_letter_or_digit = True
                        break
            if not is_letter_or_digit:
                for dc in digit_chars:
                    if char == dc:
                        is_letter_or_digit = True
                        break

            if not is_letter_or_digit:
                has_special = True
        if has_uppercase and has_lowercase and has_digit and has_special:
            break

    return has_uppercase and has_lowercase and has_digit and has_special

test_case = check_password(str(input()))
print(test_case)     