def value(colors):
    color_list=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    new_list=[]
    k=0
    for i in colors:
        if k==2:
            break
        new_list+=str(color_list.index(i))
        k+=1
    temp=''
    for i in new_list:
        temp+=i
    return int(temp)
        