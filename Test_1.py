def even(x):
    if x & 1:
        return 'odd'
    else:
        return 'even'

print(even(9))

#The bitwise operation is slightly faster than the % operator. The difference is not a big one and it can be neglected.
#Most people use the "%" way instead of the bitwise beacuse it is more user friendly.