__author__ = 'lois'

"""
a,b=0,1
while b<10:
    print(b)
    a , b = b , a + b

i=256*256
print('the value of i is',1)


a,b=0,1
while b<1000:
    print(b,end=',')
    a , b = b , a + b



x= int(input("please enter an integer:"))
#please enter integer:42
if x < 0:
    x = 0
    print('negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')
"""
#measure some strings
words=['cat','window','defenestrate']
for w in words:
    print(w,len(w))

for w in words[:]:#loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0,w)
        print(words)

for i in range(5):
    print (i)
