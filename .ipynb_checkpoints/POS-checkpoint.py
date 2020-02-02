# _*_ coding: utf-8 _*_
# @Time   : 2019/12/28 2:04 下午 
# @Author : 邵泽志 
# @File   : POS.py
# @Desc   : 


import random

c1 = 2
c2 = 2


def f_x(x):
    """
    适应度函数
    """
    return x * x * x - 5 * x * x - 2 * x + 3


def POS(x_i, i):
    """
    输入粒子x_i
    """
    if x_i >= 5 or x_i <= -2:
        return
    global g_best, p_best, c1, c2, g_best_x, p_best_x
    p_current = f_x(x_i)
    if p_current > p_best[i]:
        p_best[i] = p_current  # 存储y坐标
        p_best_x[i] = x_i
    if p_current > g_best:
        g_best = p_current
        g_best_x = x_i
    v_i_plus_1 = v[i] + c1 * random.random() * (p_best_x[i] - x_i) + \
                 c2 * random.random() * (g_best_x - x_i)
    v[i] = v_i_plus_1
    x_i_plus_1 = x_i + v_i_plus_1
    p[i] = x_i_plus_1


p = [(random.random() * 7 - 2) for i in range(0, 4)]  # 产生四个横坐标
v = [0, 0, 0, 0]

g_best = 3
g_best_x = 0

p_best_x = [p[i] for i in range(0, 4)]
p_best = [f_x(p[i]) for i in range(0, 4)]

for i in range(0, 100):
    # 迭代100轮
    for i in range(0, 4):
        POS(p[i], i)
    print(p)

print("###################              结果输出                 #####################")

print("最大值坐标=" + str(g_best_x))
print("最大值=" + str(g_best))

print("四个粒子的最优坐标" + str(p_best_x))
print("四个粒子的最优值" + str(p_best))
