n=int(input())
def p():
    i=1
    while i<=n:
        yield i
        i=i+1
for i in p():
    if i%2==0:
        print(i, end=',')