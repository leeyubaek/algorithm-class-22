import time
from timeit import default_timer as timer

# 테스트 케이스 (전역 변수)
TEST_VALUES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# 반복문 방식 팩토리얼
def factorial_iter(n) -> int:
    if n < 0:
        raise ValueError("정수 (0 이상의 숫자)만 입력하세요")
    
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


# 재귀 방식 팩토리얼
def factorial_rec(n) -> int:
    if n < 0:
        raise ValueError("정수 (0 이상의 숫자)만 입력하세요")
    
    if n == 1 or n == 0:
        return 1
    else :
        return n * factorial_rec(n-1)


# 실행 시간 측정 함수
def run_with_time(func, n: int):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    elapsed = end - start
    return result, elapsed

# 정수 입력 검증 함수
def input_integer(prompt="정수를 입력하세요: "):
    user_input = input(prompt)
    if not user_input.isdigit():
        print("정수 (0 이상의 숫자)만 입력하세요")
        return None
    return int(user_input)

# 메뉴 실행
def show_menu():
    print("\n====== 팩토리얼 계산기 ======")
    print("1. 반복문으로 n! 계산")
    print("2. 재귀로 n! 계산")
    print("3. 두 방식 모두 계산 후 결과/시간 비교")
    print("4. 준비된 테스트 데이터 일괄 실행")
    print("q. 종료")
    print("==============================")

def run_single(mode: int):
    n = input_integer("n 값을 입력하세요: ")
    if n is None:
        return

    try:
        if mode == 1:
            result, t = run_with_time(factorial_iter, n)
            print(f"[반복] {n}! = {result}")
            print(f"실행 시간: {t:.6f}초")
        elif mode == 2:
            result, t = run_with_time(factorial_rec, n)
            print(f"[재귀] {n}! = {result}")
            print(f"실행 시간: {t:.6f}초")
        elif mode == 3:
            res_iter, t_iter = run_with_time(factorial_iter, n)
            try:
                res_rec, t_rec = run_with_time(factorial_rec, n)
                match = res_iter == res_rec
            except RecursionError:
                res_rec = "RecursionError"
                t_rec = 0
                match = False
            print(f" - [반복] {n}! {res_iter}")
            print(f" - [재귀] {n}! {res_rec}")
            print(f" - 결과 일치 여부: {' 일치' if match else ' 불일치'}")
            print(f" - [반복]: ( {t_iter:.6f}초) | [재귀]: ( {t_rec:.6f}초)")
            
    except ValueError as ve:
        print(f"Error: {ve}")

def run_batch_test():
    print("\n[ 테스트 케이스 일괄 실행 ]")
    for n in TEST_VALUES:
        print(f"\n n = {n}")
        try:
            res_iter, t_iter = run_with_time(factorial_iter, n)
        except Exception as e:
            res_iter, t_iter = f"Error: {e}", 0

        try:
            res_rec, t_rec = run_with_time(factorial_rec, n)
        except RecursionError:
            res_rec, t_rec = "RecursionError", 0
        except Exception as e:
            res_rec, t_rec = f"Error: {e}", 0

        match = res_iter == res_rec
        print(f" - [반복]: {n}! {res_iter}")
        print(f" - [재귀]: {n}! {res_rec}")
        print(f" - [반복]: ( {t_iter:.6f}초) | [재귀]: ( {t_rec:.6f}초)")

# 메인 루프
def main():
    while True:
        show_menu()
        choice = input("메뉴 선택 >> ")
        if choice == "q":
            print("프로그램을 종료합니다.")
            break
        elif choice in ["1", "2", "3"]:
            run_single(int(choice))
        elif choice == "4":
            run_batch_test()
        else:
            print("잘못된 입력입니다. 0~4 중 선택하세요.")

if __name__ == "__main__":
    main()