# 1874. 스택 수열
'''
- 스택 자료구조는 LIFO형태로 선입후출 특성
- 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어 놓음으로써 하나의 수열을 만들 수 있음
- 이 때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 함

Q. 임의의 수열이 주어졌을 때, 스택을 이용해 그 수열을 만들수 있는지 없는지,
있다면 어떤 순서로 push와 pop을 수행해야 하는지 알 수 있는데 이를 계산하는 프로그램을 만들기

- 입력: 첫 줄에 n이 주어짐, 둘째줄부터 n개의 줄에 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어짐
'''

#풀이

n = int(input())

stack = [] #오름차순으로 값을 1~n까지 push
ans = [] #+, - 로 push와 pop을 append

th = 1 #회수
for _ in range(n):
  nums = int(input())

  while th <= nums:   #th가 nums보다 작거나 같으면,
    stack.append(th)  #stack에 th를 push함
    ans.append('+')   #답이 되는 ans에는 "+"를 push함
    th += 1
  
  if stack[-1] == nums: #stack의 top의 숫자가 nums와 같으면 stack.pop()을 하고,
    stack.pop()
    ans.append('-')     #답이 되는 ans에 "-"를 push함

if len(stack) >= 1: #모든 연산 수행 후, stack에 수가 남아 있으면, NO를 출력
  print('NO')

else:
  for j in ans:
    print(j)