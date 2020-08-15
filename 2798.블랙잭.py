N, M = map(int,input().split())
black = 0

arr = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if(i==j or j==k or i==k):
                continue
            if((arr[i]+arr[j]+arr[k] <= M) and (arr[i]+arr[j]+arr[k] > black)):
                black = arr[i]+arr[j]+arr[k]

print(black)
