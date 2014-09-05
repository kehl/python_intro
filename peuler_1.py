__author__ = 'lois'


sum= 0
for x in range(1, 1000):
    # if x is divisible by 3 or by 5
    if (x % 3 == 0  or x % 5 == 0):
        sum = sum + x

print (sum)

