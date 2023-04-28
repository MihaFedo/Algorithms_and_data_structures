n = int(input())
arr_1 = list(map(int, input().split()))
k = int(input())

previous=set()
result=[]
a=0

for i in range(0,n):
    if k-arr_1[i] in previous:
        result=[k-arr_1[i],arr_1[i]]
        a=1
        break
    else:
        previous.add(arr_1[i])

if a==1:
    print(" ".join(list(map(str, result))))
else:
    print("None")