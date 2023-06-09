def Powers(num,expo_pow):
    if expo_pow==0:
        return 1
    else:
        return num*Powers(num,expo_pow-1)
    



value=Powers(2,5)
print(value)    