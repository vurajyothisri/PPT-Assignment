def Not_In_List(nums1,nums2):
    result=[[],[]]
    for i in nums1:
        if i not in nums2:
            result[0].append(i)
    for i in nums2:
        if i not in nums1:
            result[1].append(i) 
    return result



value=Not_In_List(nums1 = [1,2,3], nums2 = [2,4,6])
print(value)