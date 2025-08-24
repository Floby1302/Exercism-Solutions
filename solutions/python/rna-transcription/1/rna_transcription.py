def to_rna(dna_strand):
    result=''
    temp=list(dna_strand)
    for i in range(0,len(temp)):
        if temp[i]=='C':
            result+='G'
        if temp[i]=='G':
            result+='C'
        if temp[i]=='T':
            result+='A'
        if temp[i]=='A':
            result+='U'
    return result
