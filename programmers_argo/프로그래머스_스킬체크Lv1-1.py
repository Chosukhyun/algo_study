# 문제 1
'''
정수n을 입력받아 n의 약수를 더한 값을 리턴하는 함수, solution을 완성하기
- 입출력 예 : 12의 약수는 1, 2, 3, 4, 6, 12이고, 모두 더하면 28
- 풀이 생각하기 : 1 ~ n+1 중 나누어서 나머지가 0이면 answer에 더해줌
'''
def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    
    return answer