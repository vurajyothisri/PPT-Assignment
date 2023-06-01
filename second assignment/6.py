def Find_index(numbers,target):
    first=0
    last=len(numbers)-1
    while first<last:
          mid=(first+last)//2
          if numbers[mid]==target:
               return mid
          elif numbers[mid]<target:
               first=mid+1
          else:
                last=last-1
    return -1



value=Find_index([-1,0,3,5,9,12],10)
print(value)

            
               