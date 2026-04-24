# x**2 + y**2 = 1
# f(x, y) = e**y * cos(x) 의 최소값

import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    return np.exp(x[1]) * np.cos(x[0])

def constraint(x):
    return x[0]**2 + x[1]**2 - 1

# 초기 추정값
initial_guess = [0.5, 0.5]
# 제약 조건 정의
constraints = {'type': 'eq', 'fun': constraint}
# 최적화 수행
result = minimize(objective_function, initial_guess, constraints=constraints)
print("최적화 결과:", result)
print("최소값:", result.fun)
print("최적 해:", result.x)