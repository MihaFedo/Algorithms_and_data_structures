n = int(input())
arr_1 = list(map(int, input().split()))
k = int(input())

a=0
result=[]

for i in range(0, n):
    for j in range(i+1,n):
        if arr_1[i]+arr_1[j]==k:
            a=1
            result=[arr_1[i],arr_1[j]]
            break
    if a==1:
        break

if a==1:
    print(" ".join(list(map(str, result))))
else:
    print("None")