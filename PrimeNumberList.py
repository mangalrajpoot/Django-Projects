x=[1,2,3,4,5,6,7,8,9]
b=[]
for a in x:
    if a>1:
        for i in range(2,a):
            if(a%i==0):
                break
        else:
            b.append(a)
print(b)
    
