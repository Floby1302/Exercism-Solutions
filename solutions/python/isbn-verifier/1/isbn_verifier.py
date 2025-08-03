def is_valid(isbn):
    sum=0
    j=10
    temp='abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    for i in isbn:
        if i in temp:
            return False
            
    if isbn.endswith('X'):
        for i in isbn:
            if i.isdigit()==True:
                sum+=int(i)*j
                j-=1
        sum+=10
        j-=1
        if sum % 11==0 and j==0:
            return True
        return False   
        
    for i in isbn:
        if i.isdigit()==True:
                sum+=int(i)*j
                j-=1
    if sum % 11==0 and j==0:
        return True
    return False