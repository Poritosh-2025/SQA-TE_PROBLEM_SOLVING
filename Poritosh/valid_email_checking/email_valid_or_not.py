def valid_mail(email):
    has_at = False
    at_position = -1
    index = 0

    for char in email:
        if char == '@':
            has_at = True
            at_position = index
            break
        index = index + 1

    if not has_at:
        return False
    
    has_dot_after_at = False
    dot_position = -1
    index = at_position + 1
    
    while index < len(email):
        if email[index] == '.':
            has_dot_after_at = True
            dot_position = index
            break
        index = index + 1
    
    if not has_dot_after_at:
        return False
    
    local_part = ""
    i = 0
    while i < at_position:
        local_part = local_part + email[i]
        i = i + 1
    domain_part = ""

    i = at_position + 1
    while i < len(email):
        domain_part = domain_part + email[i]
        i = i + 1

    top_level_domain = ""
    i = dot_position + 1
    while i < len(email):
        top_level_domain = top_level_domain + email[i]
        i = i + 1

    if len(local_part) == 0:
        return False
    
    if len(domain_part) == 0:
        return False
    if len(top_level_domain) <2:
        return False
    
    for char in local_part:
        char_code = ord(char)
        if not ((char_code >=97 and char_code <= 122) or (char_code >= 48 and char_code <= 57) or char == '.' or char == '_' or char == '-'):
            return False
        
    for char in domain_part:
        char_code = ord(char)
        if not ((char_code >= 97 and char_code <= 122) or (char_code >= 48 and char_code <= 57) or char == '.' or char == '-'):
            return False
    if local_part[0] == '.' or local_part[0] == '-' or local_part[0] == '_':
        return False
    if local_part[-1] == '.' or local_part[-1] == '-' or local_part == '_':
        return False
    if domain_part[0] == '.' or domain_part[0] == '-':
        return False
    if domain_part[-1] == '.' or domain_part[-1] == '-':
        return False
    return True

input_email =  valid_mail(str(input()))
print(input_email)


