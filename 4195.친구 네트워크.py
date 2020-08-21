n = int(input())

for i in range(n):
    friends = set([])
    f = int(input())
    for j in range(f):
        member = list(input().split())
        friends.update(member)
        print(len(friends))
