# 0/1 Knapsack Problem - Bottom-up DP + Backtracking

def knapSack_dp(W, wt, val, n):
    A = []
    for i in range(n + 1):
        row = []
        for w in range(W + 1):
            row.append(0)
        A.append(row)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if w < wt[i - 1]:
                A[i][w] = A[i - 1][w]
            else:
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)

    return A[n][W], A


# 물건 정보
items = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4)
]

wt = [3, 1, 2, 2, 1]
val = [12, 10, 6, 7, 4]
n = len(items)

# 사용자 입력
print("<입력>")
W = int(input("배낭 용량을 입력 하세요 : "))
print("<프로그램 실행>")
# DP 실행
max_value, A = knapSack_dp(W, wt, val, n)
print("최대 만족도 =", max_value)


# =======================
# 선택된 물건 역추적
# =======================
selected = []
w = W

for i in range(n, 0, -1):
    if A[i][w] != A[i - 1][w]:
        name, weight, value = items[i - 1]
        selected.append(name)
        w -= weight

selected.reverse()

print("선택된 물건:", selected)
