def classify(number):
    list=[]
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number-1):
        if number % i ==0:
            list.append(i)
    sum=0
    for i in list:
        sum+=i
    if sum==number:
        return 'perfect'
    if sum>number:
        return 'abundant'
    return 'deficient'
