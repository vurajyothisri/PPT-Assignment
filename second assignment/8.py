
def Difference(nums,k):
    n=len(nums)
    minimum=float('inf')
    copy_nums=nums.copy()
    print("copy:",copy_nums)
    
    for i in range(n):  
        for j in range(-k,k+1):
            nums[i]=copy_nums[i]+j
            minimum=min(minimum,(max(nums)-min(nums)))
        print("modified:",nums) 
        print("minimum:", minimum)   
       
    return minimum


value=Difference([2, 12, 34, 97, 10],2)
print(value)