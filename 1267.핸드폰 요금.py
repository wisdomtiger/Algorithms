a = int(input())
arr = list(map(int, input().split()))
y = 0
m = 0

for i in arr:
    y += (int(i/30)+1)*10
    m += (int(i/60)+1)*15

if(y<m):
    print("Y",y)
elif(y==m):
    print("Y","M",y)
else:
    print("M",m)