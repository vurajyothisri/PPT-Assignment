def Monotonic(nums):

    Monotonicornot1=[]
    Monotonicornot2=[]
#    for increasing one
    for i in range(len(nums)-1):
         
        if nums[i]<=nums[i+1]:
            Monotonicornot1.append(True)
        else:
            Monotonicornot1.append(False)   
    # for decreasing one    
    for i in range(len(nums)-1):
          
        if nums[i]>=nums[i+1]:
            Monotonicornot2.append(True)
        else:
            Monotonicornot2.append(False)     
       
            

       

    find1=all(Monotonicornot1)
    find2=all(Monotonicornot2)

    return find1 or find2


value=Monotonic([1,2,2,3])
print(value)