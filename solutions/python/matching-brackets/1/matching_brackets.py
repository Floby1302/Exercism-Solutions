def is_paired(input_string):
    st = []  
    for c in input_string:
        if c in '({[': 
            st.append(c)
        elif c in ')}]':  
            if not st or (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c ==']' and st[-1]!='['):
                return False
            st.pop()
    if not st:
        return True 
    return False