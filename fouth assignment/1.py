def Common_numbers(num1,num2,num3):
    common=[]
    for i in num1:
        if (i in num2) and (i in num3):
            common.append(i)
    sorted_common=sorted(common)        
    return sorted_common



value=Common_numbers(num1 = [1,2,3,4,5], num2 = [1,2,5,7,9], num3 = [1,3,4,5,8])    
print(value)