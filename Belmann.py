# _*_ coding: utf-8 _*_
# @Time   : 2020/1/4 4:06 下午 
# @Author : 邵泽志 
# @File   : Belmann.py
# @Desc   :
import copy


def update(A, A_next):
    for i in range(0, len(A)):
        if i == 0:
            A_next[i] = 1 / 4 * (-1 + 0) + \
                        1 / 4 * (-1 + A[i]) + \
                        1 / 4 * (-1 + A[i + 1]) + \
                        1 / 4 * (-1 + A[i])
        if i == 1:
            A_next[i] = 1 / 4 * (-1 + A[i - 1]) + \
                        1 / 4 * (-1 + A[i + 1]) + \
                        1 / 4 * (-1 + A[i + 2]) + \
                        1 / 4 * (-1 + A[i])
        if i == 2:
            A_next[i] = 1 / 4 * (-1 + 0) + \
                        1 / 4 * (-1 + A[i]) + \
                        1 / 4 * (-1 + A[i - 1]) + \
                        1 / 4 * (-1 + A[i])
        if i == 3:
            A_next[i] = 1 / 4 * (-1 + A[i - 2]) + \
                        1 / 4 * (-1 + A[i]) + \
                        1 / 4 * (-1 + A[i]) + \
                        1 / 4 * (-1 + A[i])
    A = copy.deepcopy(A_next)
    out_print(A)
    return A, A_next

def out_print(A):
    print(str(A[0]) + " " + str(A[1]) + " " + str(A[2]))
    print(str(A[3]))


if __name__ == "__main__":

    A = [0, 0, 0, 0]
    A_next = [0, 0, 0, 0]

    while True:
        A, A_next = update(A, A_next)
    a = 1
