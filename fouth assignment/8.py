def combine(nums,n):
    combines_arr=[]
    x=nums[0:n]
    y=nums[n:len(nums)]
    print("x:",x)
    print("y:",y)
    for i in range(n):
        combines_arr.append(x[i])
        combines_arr.append(y[i])
    return combines_arr



value=combine(nums=[2,5,1,3,4,7],n=3)
print(value)    