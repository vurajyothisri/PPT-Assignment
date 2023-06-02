def Unique_one(nums):
    result=0
    for i in nums:
        result^=i
    return result
    
value=Unique_one([2,2,1,10,9,1,4,9,4])  
print(value)              