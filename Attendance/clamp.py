#Pohsun Chang
#830911
#MSITM6341
#11/19/2019


def clamp(value, min, max):   
    if value < min:
        return min
    elif max < value:
        return max
    else:
        return value

print(clamp(12, 0, 20))


