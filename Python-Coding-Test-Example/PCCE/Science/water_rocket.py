# 물로켓 최대 높이 계산 예제

def calculate_height(initial_velocity):
    '''
    initital_velocity: 초기 속도, 단위 m/s
    return: 최대 높이, 단위 m
    '''

    g = 9.8 # 중력가속도 m/s^2
    height = (initial_velocity ** 2) / (2 * g)

    return height