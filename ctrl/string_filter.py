
def check_string(base_string: str, key: str):
    if key in base_string:
        return True
    else:
        return False
        
def check_title(filter_strs, title_tokens):
    for word in filter_strs:
        if word in title_tokens:
            return True
    return False