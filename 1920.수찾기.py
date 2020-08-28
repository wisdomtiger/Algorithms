n = int(input())
a = set(map(int,input().split()))  ### set의 효과가 뭐지..?
m = int(input())
x = list(map(int,input().split()))

for i in x:

    if(i in a):
        print(1)
    else:
        print(0)
