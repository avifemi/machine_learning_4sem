import numpy as np
print("Выберете задание(цифра от 1 до 5)")
num = int(input())
match num:
  case 1:
    rows, cols = map(int, input("Введите количество строк и столбцов через пробел: ").split())
    print("Введите элементы массива построчно, через пробел:")
    matrix = np.array([list(map(int, input().split())) for i in range(rows)])
    row_index, col_index = map(int, input("Введите индекс строки и столбца элемента через пробел: ").split())

    def get_neighbors_indices(matrix, row, col):
        rows, cols = matrix.shape
        neighbors = []
        shifts = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
        for a, b in shifts:
            new_row, new_col = row + a, col + b
            if 0 <= new_row < rows and 0 <= new_col < cols:
                neighbors.append((new_row, new_col))
        return np.array(neighbors)
    neighbors = get_neighbors_indices(matrix, row_index, col_index)
    print("Индексы соседних элементов", neighbors)
  case 2:
    A = np.random.randint(-100, 100, 10)
    B = np.random.randint(-100, 100, 10)
    C = np.array([a + B[np.abs(B - a).argmin()] for a in A])
    print("Массив C", C)
  case 3:
    sales = np.array([
    [120, 340, 560, 230],
    [150, 400, 600, 280],
    [180, 390, 630, 310],
    [170, 420, 670, 290],
    [200, 450, 710, 330],
    [220, 470, 750, 350],
    ])
    print("Общий объем продаж за 6 месяцев", np.sum(sales))
    max_sum = np.sum(sales, 1)
    print("Максимальный объем продаж был в", np.argmax(max_sum) + 1, "месяце")
    max_product = np.sum(sales, 0)
    average_product = max_product.mean()
    product_upper_avg = np.where(max_product > average_product)[0] +1
    print("Товары с большими объемами продаж", product_upper_avg)
    print("Средний объем продаж электроники", np.mean(sales, 0)[0])
    print("Средний объем продаж одежды", np.mean(sales, 0)[1])
    print("Средний объем продаж бытовой техники", np.mean(sales, 0)[2])
    print("Средний объем продаж мебели", np.mean(sales, 0)[3])

    print("Продажа электроники по сравнению с началом года изменилась на", ((sales[5][0] * 100) / sales[0][0] - 100) , "%")
    print("Продажа одежды по сравнению с началом года изменилась на", ((sales[5][1] * 100) / sales[0][1] - 100) , "%")
    print("Продажа электроники по сравнению с началом года изменилась на", ((sales[5][2] * 100) / sales[0][2] - 100) , "%")
    print("Продажа электроники по сравнению с началом года изменилась на", ((sales[5][3] * 100) / sales[0][3] - 100) , "%")
  case 4:
    sales = np.random.randint(500, 1500, (3, 12))
    print("Средние продажи за 2022 год", sales.mean(1)[0])
    print("Средние продажи за 2023 год", sales.mean(1)[1])
    print("Средние продажи за 2024 год", sales.mean(1)[2])

    max_index22 = np.argmax(sales, 1)[0] +1
    max_index23 = np.argmax(sales, 1)[1] +1
    max_index24 = np.argmax(sales, 1)[2] +1
    print("В", max_index22,"месяце был самый большой прирост продаж в 2022 году" )
    print("В", max_index23,"месяце был самый большой прирост продаж в 2023 году" )
    print("В", max_index24,"месяце был самый большой прирост продаж в 2024 году" )

    A = np.array([[2022], [2023], [2024]])
    A = np.column_stack((A, np.ones(A.shape[0]))) #добавляем столбец единиц для учета смещения
    b = sales.mean(1)
    x, _, _, _ = np.linalg.lstsq(A, b, rcond=None) #система наименьших квадратов
    a, c = x #ax + c
    year_2025 = np.array([[2025, 1]])
    prediction_25 = a * 2025 + c
    print("Предсказание продаж на 2025 год", prediction_25)
  case 5:
    temperatures = np.random.randint(-10, 36, size=365)
    average_temperature = temperatures.mean()
    print("Средняя температура в течение года", average_temperature)

    days_above_avg = np.where(temperatures > average_temperature)[0] +1
    days_below_avg = np.where(temperatures < average_temperature)[0] +1
    print("Дни, когда температура была выше среднего", days_above_avg)
    print("Дни, когда температура была ниже среднего", days_below_avg)

    min_temp_index = np.argmin(temperatures)
    max_temp_index = np.argmax(temperatures)
    print("Минимальная температура в году была в", min_temp_index +1, "день")
    print("Максимальная температура в году была в", max_temp_index +1, "день")

    lower_bound = average_temperature - 2
    upper_bound = average_temperature + 2
    months = np.array_split(temperatures, 12)
    cold_month=[]
    norm_month=[]
    warm_month=[]
    for i, month in enumerate(months, start=1):
      avarage_month = month.mean()
      if(avarage_month > upper_bound):
        warm_month.append(i)
      elif(avarage_month < lower_bound):
        cold_month.append(i)
      elif(avarage_month >= lower_bound and avarage_month <= upper_bound):
        norm_month.append(i)
    print("Холодные месяца", cold_month)
    print("Нормальные месяца", norm_month)
    print("Теплые месяца", warm_month)
