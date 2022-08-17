#자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수

'''
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
'''
#생각해보기
# 자연수 n을 이진수로 변환하여, 0과 1중 1만 추가하여 리스트를 생성함
# while문을 사용하여 n보다 큰수이고, 1의 개수가 같으면 answer을 반환하고 종료

# 문제풀이
def solution(n):
    answer = 0
    bi = bin(n)  #bi: 자연수 n을 이진수로 변환
    lst_n = [int(one) for one in bi if one == '1']  # 이진수로 변환한 자연수 n에서 1만 추가하여 lst_n을 생성
    
    big = 1
    while n <  n+big:
        
        lst_big = [int(b) for b in bin(n+big) if b == '1']
        #n과 n보다 큰 자연수의 이진수로 표현했을 때, 1의 개수가 다르면 big에 1을 더하며 반복
        if len(lst_big) != len(lst_n):
            big += 1

        #n과 n보다 큰 자연수의 이진수로 표현했을 때, 1의 개수가 같으면 반복을 종료하고 answer을 반환    
        elif len(lst_big) == len(lst_n):
            answer = n + big
            break
            
    return answer