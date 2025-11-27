import random

# print("--- 1: Симметрия относительно главной диагонали ---")

# matrix1 = [[random.randint(0, 100) for _ in range(5)] for _ in range(5)]

# print("Исходная матрица:")
# for row in matrix1:
#     print(row)


# for i in range(5):
#     for j in range(i + 1, 5):
#         matrix1[i][j], matrix1[j][i] = matrix1[j][i], matrix1[i][j]

# print("\nМатрица после:")
# for row in matrix1:
#     print(row)
# print("\n" + "="*30 + "\n")

# print("--- 2: Обмен главной и побочной диагоналей ---")

# matrix2 = [[random.randint(0, 100) for _ in range(5)] for _ in range(5)]

# print("Исходная матрица:")
# for row in matrix2:
#     print(row)

# n = 5 
# for i in range(n):
#     matrix2[i][i], matrix2[i][n - 1 - i] = matrix2[i][n - 1 - i], matrix2[i][i]

# print("\nМатрица после:")
# for row in matrix2:
#     print(row)
# print("\n" + "="*30 + "\n")

print("--- 3: Сумма между Min и Max ---")

matrix3 = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]

print("Матрица:")
for row in matrix3:
    print(row)

flat_list = []
for row in matrix3:
    for num in row:
        flat_list.append(num)

min_val = min(flat_list)
max_val = max(flat_list)

idx_min = flat_list.index(min_val)
idx_max = flat_list.index(max_val)

print(f"\nМинимум: {min_val} (индекс {idx_min})")
print(f"Максимум: {max_val} (индекс {idx_max})")

start = min(idx_min, idx_max)
end = max(idx_min, idx_max)

elements_between = flat_list[start + 1 : end]
result_sum = sum(elements_between)

print(f"Элементы между ними: {elements_between}")
print(f"Сумма элементов: {result_sum}")