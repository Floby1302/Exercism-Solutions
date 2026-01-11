def label(colors):
    color_list=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    temp=[]
    for i in colors:
        temp.append(color_list.index(i))
    resistance=(temp[0]*10+temp[1])*(10**temp[2])
    if resistance>10**9:
        return str(int(resistance/(10**9))) + ' gigaohms'
    if resistance>10**6:
        return str(int(resistance/(10**6))) + ' megaohms'
    if resistance>10**3:
        return str(int(resistance/(10**3))) + ' kiloohms'
    return str(int(resistance)) + ' ohms'
        
