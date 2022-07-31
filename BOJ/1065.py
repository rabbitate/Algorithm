# https://www.acmicpc.net/problem/1065

# # 한 수인지 검사하는 함수
# def check(num):
#     l = []
#     while num >= 10:
#         l.append(num%10)
#         num //= 10
    
#     l.append(num)

#     if len(l) == 3:
#         if (l[0]+l[2])/2 == l[1]: return True
#         else: return False
#     elif len(l) == 1 or len(l) == 2: return True
#     else: return False

n = int(input())
cnt = 0 # 한 수 개수

for i in range(1,n+1):
    if 100 <= i <= 999:
        if (i//100+i%10) == (i//10%10): cnt += 1
    elif i == 1000: pass
    else: cnt += 1

print(cnt)
