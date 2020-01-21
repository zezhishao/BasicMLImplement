# _*_ coding: utf-8 _*_
# @Time   : 2019/12/28 8:01 下午 
# @Author : 邵泽志 
# @File   : SimpleBandit.py
# @Desc   :
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import time

mu = [0.13, 0.50, -1.21, 0.73, 1.6, 1.12, -1.25, -2.45, -0.86, 1.39]
a = sum(mu)/10
print(a)
N = 1000


def bandit(a):
    """
    使用行动a进行赌博
    :param a:行动
    :return:
    """
    reward = np.random.normal(mu[a], 1, 1)
    return reward[0]


def get_UCB(N_a, n):
    UCB = [0 for i in range(0, len(N_a))]
    c = 0.2
    if n == 0:
        return UCB
    for i in range(0, len(N_a)):
        if N_a[i] == 0:
            UCB[i] = 0
        else:
            c * math.sqrt(math.log(n) / N_a[i])
    return UCB


def bandit_algorithm_with_e_with_UCB(e):
    result = []
    c = 1
    # 没有乐观选择策略的简单赌博机策略
    # Q_a = [0 for i in range(0, 10)]
    # N_a = [0 for i in range(0, 10)]
    # 乐观选择策略的简单赌博机策略，使用此方法，能够让更多的action在初期被探索，让整个过程更加平稳，最终结果更加正确。
    Q_a = [10 for i in range(0, 10)]
    N_a = [0 for i in range(0, 10)]
    Average_Reward = 0
    n = 0
    while True:
        if n == N:
            break
        # 使用UCB
        UCB = get_UCB(N_a, n)
        A1 = Q_a.index(max([Q_a[i] + UCB[i] for i in range(0, len(Q_a))]))
        A2 = Q_a.index(random.choice(Q_a))
        r = np.random.uniform(0, 1, 1)[0]
        if r > e:
            A = A1
        else:
            A = A2
        R = bandit(A)
        N_a[A] += 1
        Q_a[A] = Q_a[A] + 1 / N_a[A] * (R - Q_a[A])
        n += 1
        Average_Reward = Average_Reward + 1 / n * (R - Average_Reward)
        result.append(Average_Reward)
    return result


def bandit_algorithm_with_e_with_greedy(e):
    result = []
    c = 0.1
    # 没有乐观选择策略的简单赌博机策略
    # Q_a = [0 for i in range(0, 10)]
    # N_a = [0 for i in range(0, 10)]
    # 乐观选择策略的简单赌博机策略，使用此方法，能够让更多的action在初期被探索，让整个过程更加平稳，最终结果更加正确。
    Q_a = [5 for i in range(0, 10)]
    N_a = [0 for i in range(0, 10)]
    Average_Reward = 0
    n = 0
    while True:
        if n == N:
            break
        # 使用贪心策略
        A1 = Q_a.index(max(Q_a))
        A2 = Q_a.index(random.choice(Q_a))
        r = np.random.uniform(0, 1, 1)[0]
        if r > e:
            A = A1
        else:
            A = A2
        R = bandit(A)
        N_a[A] += 1
        Q_a[A] = Q_a[A] + 1 / N_a[A] * (R - Q_a[A])
        n += 1
        Average_Reward = Average_Reward + 1 / n * (R - Average_Reward)
        result.append(Average_Reward)
    return result


if __name__ == "__main__":
    e = 0.1
    result1 = bandit_algorithm_with_e_with_greedy(0.1)

    result2 = bandit_algorithm_with_e_with_greedy(0.2)

    result3 = bandit_algorithm_with_e_with_greedy(0)

    result4 = bandit_algorithm_with_e_with_UCB(0.1)

    result5 = bandit_algorithm_with_e_with_UCB(0.2)

    plt.ion()  # 开启interactive mode 成功的关键函数
    plt.figure(1)

    plt.plot(range(1, N + 1), result1, label='e=0.1')  # 第次对画布添加一个点，覆盖式的。
    plt.draw()  # 注意此函数需要调用
    plt.plot(range(1, N + 1), result2, label='e=0.2')  # 第次对画布添加一个点，覆盖式的。
    plt.draw()  # 注意此函数需要调用
    plt.plot(range(1, N + 1), result3, label='greedy')  # 第次对画布添加一个点，覆盖式的。
    plt.draw()  # 注意此函数需要调用
    plt.plot(range(1, N + 1), result4, label='e=0.1 with UCB')  # 第次对画布添加一个点，覆盖式的。
    plt.draw()  # 注意此函数需要调用
    plt.plot(range(1, N + 1), result5, label='e=0.2 with UCB')  # 第次对画布添加一个点，覆盖式的。
    plt.draw()  # 注意此函数需要调用

    plt.legend()  # 显示图例
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')

    plt.show()
