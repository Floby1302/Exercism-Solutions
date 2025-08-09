def reverse(text):
    text_list=list(text)
    text_list.reverse()
    result=''
    print(text_list)
    for i in text_list:
        result+=i
    return result