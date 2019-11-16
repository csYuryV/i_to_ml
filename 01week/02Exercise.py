'''



Объединение матриц

Сгенерируйте две единичные матрицы (т.е. с единицами на диагонали) размера 3x3.
Соедините две матрицы в одну размера 6x3.
Функция для генерации единичной матрицы: np.eye
Аргумент: число строк (или, что эквивалентно, столбцов).
Функция для вертикальной стыковки матриц: np.vstack((A, B))


'''

import numpy as np

A = np.eye(3)
B = np.eye(3)
AB = np.vstack((A, B))

print(AB)