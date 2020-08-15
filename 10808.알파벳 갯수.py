word = str(input())
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for j in arr:
    count = 0
    for i in range(0,len(word)):
        if(j==word[i]):
            count += 1
    print(count, end = ' ')