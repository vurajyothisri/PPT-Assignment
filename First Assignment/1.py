def sum(num,sumofvalues):
    length=len(num)
    for i in range(0,length):
        for j in range(0,length):
            if num[i]+num[j]==sumofvalues:
                return [i,j]
    return []
    
    
    
value=sum([2,7,11,15],18)
print(value)