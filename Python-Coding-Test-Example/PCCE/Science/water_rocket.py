# 물로켓 최대 높이 계산 예제

def calculate_height(initial_velocity):
    '''
    initital_velocity: 초기 속도, 단위 m/s
    return: 최대 높이, 단위 m
    '''

    g = 9.8 # 중력가속도 m/s^2
    height = (initial_velocity ** 2) / (2 * g)

    return height

# 예시: 물로켓의 초기 속도가 30m/s일 때
v0 = 30 # m/s

max_height = calculate_height(v0)

print("초기 속도:", v0, "m/s")
print("예상 최대 높이:", round(max_height, 2), "m")
# round()함수는 1번 매개변수의 값을 2번 매개변수의 소수점 자리까지 반올림하는 함수다.