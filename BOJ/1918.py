# https://www.acmicpc.net/problem/1918

infix = list(input()) # 중위 표기식
postfix = [] # 후위 표기식
operator = [] # 연산자 스택

for i in infix:
    # 수식의 피연산자일 경우(수식의 피연산자는 알파벳 대문자), isalpha() 사용 가능
    if ord('A') <= ord(i) <= ord('Z'):
        postfix.append(i) # 후위 표기식에 추가
    else:
        # 여는 괄호일 경우
        if i == '(':
            operator.append(i) # 연산자 스택에 push
        # + 나 -일 경우
        elif i == '+' or i == '-':
            # + 나 -보다 우선순위가 낮은 연산자는 없으므로 모두 pop해서 추가해준다(괄호 안의 연산자가 밖의 연산자보다 우선 순위가 높으므로
            # 괄호를 만났다면 괄호 안의 연산자만 pop시켜서 추가한다)
            while operator and operator[-1] != '(':
                postfix.append(operator.pop())
            operator.append(i)
        # * 나 /일 경우
        elif i == '*' or i == '/':
            # 스택에 있던 * 니 / 만이 우선순위가 높은 연산자 이므로 스택에 peek한 연산자가 * 나 / 일 경우에선 pop시켜 추가한다
            while operator and (operator[-1] == '*' or operator[-1] == '/'):
                postfix.append(operator.pop())
            operator.append(i)
        # 괄호가 닫혔다면 괄호 안에 있는 연산자를 pop 시킨다
        elif i == ')':
            while operator[-1] != '(':
                postfix.append(operator.pop())
            operator.pop() # 여는 괄호 제거

# 연산자 스택에 남아있는 연산자를 pop 시켜준다
while operator:
    postfix.append(operator.pop())

for i in postfix:
    print(i,end="")
