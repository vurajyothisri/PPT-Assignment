def compress(chars):
    n = len(chars)
    if n == 0:
        return 0
    
    write = 0
    count = 1
    
    for i in range(1, n):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            chars[write] = chars[i-1]
            write += 1
            if count > 1:
                count_str = str(count)
                for char in count_str:
                    chars[write] = char
                    write += 1
            count = 1
    
    chars[write] = chars[n-1]
    write += 1
    if count > 1:
        count_str = str(count)
        for char in count_str:
            chars[write] = char
            write += 1
    
    return write




chars = ["a","a","b","b","c","c","c"]
result = compress(chars)
print(result)  
print(chars[:result])
