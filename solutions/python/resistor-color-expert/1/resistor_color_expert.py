def resistor_label(colors):
    color_list=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    tolerance_dict={'grey':0.05 , 'violet':0.1 , 'blue':0.25 , 'green':0.5 , 'brown':1 , 'red':2 , 'gold':5 , 'silver':10}
    if len(colors)==4:
        resistance=(10*color_list.index(colors[0])+color_list.index(colors[1]))*10**(color_list.index(colors[2]))
        if resistance>=10**9:
            if(resistance%(10**9)==0):
                return str(int(resistance/(10**9))) + ' gigaohms ±' + str(tolerance_dict[colors[3]]) + '%'
            return str(resistance/(10**9)) + ' gigaohms ±' + str(tolerance_dict[colors[3]]) + '%'
        if resistance>=10**6:
            if(resistance%(10**6)==0):
                return str(int(resistance/(10**6))) + ' megaohms ±' + str(tolerance_dict[colors[3]]) + '%'
            return str(resistance/(10**6)) + ' megaohms ±' + str(tolerance_dict[colors[3]]) + '%'
        if resistance>=10**3:
            if(resistance%(10**3)==0):
                return str(int(resistance/(10**3))) + ' kiloohms ±' + str(tolerance_dict[colors[3]]) + '%'
            return str(resistance/(10**3)) + ' kiloohms ±' + str(tolerance_dict[colors[3]]) + '%'
        return str(int(resistance)) + ' ohms ±' + str(tolerance_dict[colors[3]]) + '%'
    if len(colors)==5:
        resistance=(100*color_list.index(colors[0])+10*color_list.index(colors[1])+color_list.index(colors[2]))*10**(color_list.index(colors[3]))
        if resistance>=10**9:
            if(resistance%(10**9)==0):
                return str(int(resistance/(10**9))) + ' gigaohms ±' + str(tolerance_dict[colors[3]]) + '%'
            return str(resistance/(10**9)) + ' gigaohms ±' + str(tolerance_dict[colors[4]]) + '%'
        if resistance>=10**6:
            if(resistance%(10**6)==0):
                return str(int(resistance/(10**6))) + ' megaohms ±' + str(tolerance_dict[colors[3]]) + '%'
            return str(resistance/(10**6)) + ' megaohms ±' + str(tolerance_dict[colors[4]]) + '%'
        if resistance>=10**3:
            if(resistance%(10**3)==0):
                return str(int(resistance/(10**3))) + ' kiloohms ±' + str(tolerance_dict[colors[3]]) + '%'
            return str(resistance/(10**3)) + ' kiloohms ±' + str(tolerance_dict[colors[4]]) + '%'
        return str(int(resistance)) + ' ohms ±' + str(tolerance_dict[colors[4]]) + '%'
    if len(colors)==1:
        return str(int(color_list.index(colors[0]))) + ' ohms'