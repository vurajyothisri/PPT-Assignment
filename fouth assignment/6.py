def square(nums):
    list=[]
    for i in range(len(nums)):
        temp=nums[i]*nums[i]
        list.append(temp)
    sorted_list=sorted(list) 
    
    return sorted_list



value=square([-4,-1,0,3,10])
print(value)