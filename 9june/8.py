def Product_of_Array(nums,n):
    if n==0:
        return 1
    else:
        return nums[n]*Product_of_Array(nums,n-1)
    


value=Product_of_Array( [1, 2, 3, 4, 5],4)    
print(value)