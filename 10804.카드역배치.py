arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start_po, end_po = 0, 0

for i in range(10):
    start_po, end_po = map(int, input().split())
    if(start_po == end_po):
        continue
    start_po -= 1
    end_po -= 1

    re = int((end_po-start_po+1)/2)
    for k in range(re):
        arr[start_po], arr[end_po] = arr[end_po], arr[start_po]
        start_po += 1
        end_po -= 1

for i in arr:
    print(i, end=' ')