n=int(input())
def p():
    i=1
    while i<=n:
        yield i
        i=i+1
for i in p():
    if i%3==0:    
        print(i)
for i in p():
    if i%4==0:
        print(i)