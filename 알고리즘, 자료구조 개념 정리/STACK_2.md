# STACK_2

## 1. 계산기

#### 1) 계산기에서의 Stack의 활용

![스택이용 결과값 계산](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-01-26-image.png)

- 문자열 수식 계산의 일반적 방법
  
  __Step 1__ 중위표기법의 수식을 후위표기법으로 변경
  
  - 스택이용
  
  - 중위표기법(infix notation): 연산자를 피연산자의 가운데 표기하는 방법
    
    - ex)  A + B
  
  __Step 2__ <u>후위표기법</u>의 수식을 이용하여 계산
  
  - 후위표기법(postfix notation): 연산자를 피연산자 뒤에 표기하는 방법
    
    - ex)  A B +

#### 2) 중위표기식을 후위표기식으로 변환

- __Step 1__.  중위표기식의 후위표기식으로 변환방법 1
  
  1. 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현
  
  2. 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동
  
  3. 괄호 제거
  
  ![후위 변환](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-10-47-image.png)

- __Step 1__. 중위표기식의 후위표기식으로 변환방법 2(스택이용)
  
  1. 입력 받은 중위표기식에서 토큰을 읽음
  
  2. 토큰이 피연산자이면 토큰을 출력
  
  3. 토큰이 연산자(괄호포함)일 경우
     
     - 우선순위가 높으면 -> 스택에 push
     
     - 우선순위가 안높으면 -> 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 pop한 후 토큰의 연산자를 push
     
     - 만약 top에 연산자가 없으면 -> push
  
  4. 토큰이 오른쪽 괄호 ')'일 경우
     
     - 스택 top에 왼쪽 괄호 '('가 올 때 까지 스택에 pop을 연산을 수행
     
     - pop한 연산자를 출력
     
     - 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않음
  
  5. 중위표기식에 더 읽을 것이 없다면 중지, 더 읽을 것이 있다면 1부터 반복
  
  6. 스택에 남아있는 연산자를 모두 pop하여 출력
     
     - 스택 밖의 왼쪽 괄호는 우선순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선순위가 가장 낮음
  
  ![중위표기-> 후위표기](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-28-42-image.png)
  
  ![중위표기 -> 후위표기2](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-28-00-image.png)

#### 3) 후위표기법의 수식을 스택을 이용하여 계산

1. 피연산자를 만나면 스택에 push함

2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push함

3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력
   
   - 계산 시 주의 사항
     
     - 후위표기식을 계산 시, <u>피연산자를 스택에 쌓아 계산!!</u>

![](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-37-00-image.png)

![](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-38-05-image.png)

![](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-38-41-image.png)

![](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-39-21-image.png)

![](C:\Users\asa95\AppData\Roaming\marktext\images\2022-08-08-15-40-50-image.png)

#### 4) 수식을 eval()내장 함수로 계산

- 문자열로 된 수식을 계산 시
  
  - 스택을 두 번 사용해서 처리했던 연산을 파이썬에서 제공되는 __eval() 내장함수__ 로 계산할 수 있음
  
  - __eval(수식)__
    
    - 문자열로 된 수식을 계산함
    
    - Evaluation = '값을 구함'이라는 뜻
    
    - 올바른 수식이 아닌 경우 SyntaxError 예외가 발생함
    
    - __eval('6+5*(2-8)/2')__ 는 문자열로 된 수식의 계산결과를 반환 함

___

_____

## 2. 백트래킹
