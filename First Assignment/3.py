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
    return first



value=Find_index([1,3,5,6,10],9)
print(value)

            
               