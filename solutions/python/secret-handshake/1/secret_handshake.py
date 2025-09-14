def commands(binary_str):
    result=['wink','double blink','close your eyes','jump']
    j=0
    for i in range(len(binary_str)-1,-1,-1):
        if binary_str[i]=='1' and i!=0:
            j+=1
        if i==0 and binary_str[i]=='1':
            result.reverse()
        if binary_str[i]=='0' and j<len(result):
            result.pop(j)
    return result
        
        
                
        
        
        
