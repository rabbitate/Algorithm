#  https://www.acmicpc.net/problem/1935

n = int(input()) # 피연산자 개수
postfix = list(input()) # 후위 표기식
num = [] # 피연산자에 대응하는 값을 저장하는 리스트
stack = [] # 계산을 위한 stack

# 피연산자에 대응하는 값을 num에 저장
for _ in range(n):
    num.append(int(input()))

for i in postfix:
    # 피연산자라면
    if i.isalpha():
        # 대응하는 값을 stack에 push
        stack.append(num[ord(i)-ord('A')])
    # 연산자라면
    else:
        # 피연산자 두 개를 pop시켜 계산한 다음 stack에 push
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i == '/':
            stack.append(a/b)

print('%.2f' %stack.pop()) # 소수점 둘째 자리까지 출력
