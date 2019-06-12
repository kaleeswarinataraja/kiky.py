value12=int(input())
value22=list(map(int,input().split()))
res=0
for i in range(len(value22)-2):
    for j in range(i+1,len(value22)-1):
        for k in range(j+1,len(value22)):
            if value22[i]<value22[j]<value22[k] and i<j<k:
                res=res+1
print(res)
