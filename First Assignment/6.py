def count(nums):
    for i in nums:
        count=0
        for j in nums:
            if i==j:
                count=count+1
                
        if count>1:
            print(count)
            return True        
    return False    
            

value=count([1,2,3,4])
print(value)