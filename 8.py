def Find_missing(nums):
    values=[]
    for i in nums:
        count=0
        for j in nums:
            if i==j:
                count=count+1
                
        if count>1 and (i not in values):
            values.append(i)

    for i in range(1,len(nums)+1):
                if i not in nums:
                  values.append(i)                
            
            
   
          
    return values

Missing_number=Find_missing([1,2,2,4,5,6,8])   
print(Missing_number)     