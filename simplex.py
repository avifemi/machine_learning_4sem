from scipy.optimize import linprog
import numpy as np

print("введите номер задания")
number_task=int(input())
match number_task:
  case 1:
    #коэффициенты функции, минимизировать 1.5x + 2y + 1z
    c = [1.5, 2, 1]

    #ограничения для linprog Ax <= b (поэтому минусы появились)
    A = [
        [-12, -8, -3],
        [-9, -10, -2],
        [0, -15, -10]
    ]
    #бжу нужное нам
    b = [-60, -50, -200]

    #xyz >= 0
    x_bounds = (0, None)
    y_bounds = (0, None)
    z_bounds = (0, None)

    #решение
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='highs-ds')

    #вывод
    print("оптимальное решение:")
    print(f"количество яиц: {res.x[0]}")
    print(f"количество молока: {res.x[1]}")
    print(f"количество хлеба: {res.x[2]}")
    print(f"минимальные затраты: {res.fun} долларов")

  case 2:
    #коэффициенты функции
    c = [-10, -15]

    #ограничения левая часть
    A = [
        [2, 1],
        [1, 2]
    ]
    b = [40, 30] #ограничения правая часть

    #xy>=0
    x_bounds = (0, None)
    y_bounds = (0, None)

    #решение
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs-ds')

    #вывод
    print(f"оптимальное количество продукта A: {res.x[0]}")
    print(f"оптимальное количество продукта B: {res.x[1]}")
    print(f"максимальная прибыль: {-res.fun}")

  case 3:
    print("вы хотите максимизировать или минимизировать функцию? (пример ответа: max/min):")
    goal = input().strip().lower()

    print("введите коэффициенты функции(пример: для 6x + 9y введите: 6 9):")
    c = list(map(float, input().split()))

    #если max, меняем знак коэффициентов
    if goal == "max":
        c = [-coeff for coeff in c]

    print("введите количество ограничений:")
    k = int(input())

    A = []
    b = []

    for i in range(k):
        print("введите коэффициенты левой части (пример: для 7x + 3y введите: 7 3):")
        row = list(map(float, input().split()))
        if len(row) != len(c):
            print("количество переменных не совпадает с функцией")
            exit()
        A.append(row)

        print("введите знак ограничения (пример ответа:<= или >=):")
        sign = input().strip()

        print("введите правую часть ограничения:")
        rhs = float(input())

        #преобразование ограничений к нужной форме
        if sign == "<=":
            pass  #оставляем как есть
        elif sign == ">=":
            A[-1] = [-a for a in A[-1]]
            rhs = -rhs
        b.append(rhs)

    A = np.array(A)
    b = np.array(b)

    #x>=0
    x_bounds = [(0, None) for i in range(len(c))]

    #решение
    res = linprog(c=c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs-ds')

    #вывод
    print("\nрешение:")
    if res.success:
        for i, j in enumerate(res.x):
            print(f"x[{i + 1}] = {j:.4f}")
        target = -res.fun if goal == "max" else res.fun
        print(f"{'максимальное' if goal == 'max' else 'минимальное'} значение функции: {target:.4f}")
    else:
        print("решение не найдено :(")
