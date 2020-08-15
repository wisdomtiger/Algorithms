n = int(input())

for i in range(n):
    in_arr = input()  # 입력받는 리스트
    right_stk = []
    left_stk = []

    for a in in_arr:
        if(a == '<'):
            if(left_stk):
                right_stk.append(left_stk.pop())
        elif(a == '>'):
            if (right_stk):
                left_stk.append(right_stk.pop())
        elif(a == '-'):
            if(left_stk):
                left_stk.pop()
        else:
            left_stk.append(a)

    left_stk.extend(reversed(right_stk))
    print(''.join(left_stk))