def even(x):
    if x & 1:
        return 'odd'
    else:
        return 'even'

print(even(9))