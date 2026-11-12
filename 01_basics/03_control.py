"""01_basics · 控制流

运行：python 03_control.py

学习要点：
1. for 遍历可迭代对象，range() 生成数字序列。
2. while 适合"不知道要循环几次"的场景。
3. break 退出整个循环，continue 跳过本次。
"""


def fizzbuzz(limit: int = 15) -> list[str]:
    """经典练习：3 的倍数输出 Fizz，5 的倍数输出 Buzz，公倍数输出 FizzBuzz。

    练习：先自己写一遍，再看下面的实现对比。
    """
    result = []
    for n in range(1, limit + 1):
        if n % 15 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(n))
    return result


def multiplication_table(n: int = 9) -> None:
    """打印 n×n 乘法表。注意 end="" 用来避免换行。"""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i * j:<4}", end="")
        print()


def find_first_even(numbers: list[int]) -> int | None:
    """找到第一个偶数就返回，找不到返回 None。体会 break 的作用。"""
    for num in numbers:
        if num % 2 == 0:
            return num
    return None


def countdown(start: int = 3) -> None:
    """while 循环 + 递减。练习：用 for 实现同样效果。"""
    n = start
    while n > 0:
        print(f"倒计时 {n}")
        n -= 1
    print("发射！")


def main() -> None:
    print("--- FizzBuzz ---")
    print(" ".join(fizzbuzz()))

    print("\n--- 乘法表 ---")
    multiplication_table(5)

    print("\n--- 找第一个偶数 ---")
    print(find_first_even([1, 3, 7, 8, 10]))   # 8
    print(find_first_even([1, 3, 7]))          # None

    print("\n--- 倒计时 ---")
    countdown(3)


if __name__ == "__main__":
    main()