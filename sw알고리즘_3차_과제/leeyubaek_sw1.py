def stair_fib_dp_tab(n):
    table = [0] * (n + 1)
    table[0] = 1
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]

    return table[n], table
print("<입력>")
n = int(input("계단의 개수를 입력하시오: "))

result, table = stair_fib_dp_tab(n)
print("<프로그램 실행>")
print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")
