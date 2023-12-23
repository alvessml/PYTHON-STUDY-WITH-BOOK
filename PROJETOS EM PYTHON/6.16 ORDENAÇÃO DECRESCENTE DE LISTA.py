L=[1,2,3,4,5]
fim = 5 
while True: 
    trocou = False 
    x=0 
    while x < (fim-1): 
        if L[x] < L[x+1]: 
            trocou = True 
            temp=L[x] 
            L[x]=L[x+1]
            L[x+1]=temp
        x +=1
    if not trocou: 
        break
    False
for e in L:
    print(e)