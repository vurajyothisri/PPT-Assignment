def Candies(nums):
    length=len(nums)//2
    unique_candies=[]
    for i in range(len(nums)):
        if nums[i] not in unique_candies:
            unique_candies.append(nums[i])
    unique_candies_length=len(unique_candies)            
    return min(length,unique_candies_length)



candies=Candies([1,1,2,2,3,3,4,5,5,6])
print(candies)


