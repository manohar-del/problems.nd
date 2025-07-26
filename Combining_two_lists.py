a=float(input())
b=str(a)
c=b.index('.')
d=b[c:]
u=0
count=0
for i in range(c - 1,-1,-1):
    d=b[i]+d
    u+=1
    if (count==0 and u==3 and i!=0) or (count>0 and u==2 and i!=0):
        d=',' + d
        u=0
        count+=1
print(d)