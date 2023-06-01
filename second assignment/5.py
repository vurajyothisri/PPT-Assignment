def Max_product(nums):
    nums.sort()
    
    max1=nums[-1]*nums[-2]*nums[-3]
    
    max2=nums[0]*nums[1]*nums[-1]
    
    return max(max1,max2)


value=Max_product([12,56,90,129,89,900])
print(value)