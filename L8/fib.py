from itertools import accumulate

n = 10
start = 1  # 0|1 - з чого починаємо
print([i[start]for i in accumulate(range(n - 1), lambda s, _: (s[1], s[0] + s[1]), initial=(0, 1))])