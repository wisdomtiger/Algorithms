n = int(input())

member = []

for i in range(n):
    arr = []
    age, name = input().split()
    age = int(age)
    arr = [age,name]
    member.append(arr)

member = sorted(member,key = lambda x : x[0])  ## 정렬 조건걸기
for i in member:
    print(i[0], i[1])