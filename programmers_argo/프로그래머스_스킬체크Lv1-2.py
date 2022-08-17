#자연수 n이 매개변수로 주어짐
#n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수x를 return하도록 solution함수를 완성하기
# 답이 항상 존재함은 증명될수 있음


# 문제풀이

def solution(n):
    answer = 0
    for  x in range(1, n + 1):  #1부터 n까지..
        if n % x == 1:          # n을 x로 나누었을때 나머지가 1이면..
            answer += x         # x를 answer에 더해주고..
            break               # 중단하고 answer을 반환함
    
    return answer