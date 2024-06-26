n=int(input())
def s():
    i=1
    while True:
        if i>=n:
            break
        yield i*i
        i+=1
for i in s():
    print(i)