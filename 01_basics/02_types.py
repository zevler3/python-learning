"""01_basics · 变量与类型

运行：python 02_types.py

学习要点：
1. Python 是动态类型，变量本身没有类型，值才有。
2. type(x).__name__ 能拿到类型名，调试时很有用。
3. f-string 是首选格式化方式：f"{值:格式说明}"。
"""


def show_types() -> None:
    """打印一组值的类型，建立直观印象。"""
    samples = [42, 3.14, "Python", True, None, [1, 2], {"a": 1}, (1,)]
    for value in samples:
        # {value!r:<18} 表示：用 repr 显示、左对齐、占 18 列
        print(f"{value!r:<18} -> {type(value).__name__}")


def format_money(amount: float, currency: str = "CNY") -> str:
    """把 1234.5 变成 'CNY 1234.50'。

    练习：改一改格式说明符试试
    - {amount:,.2f}  加千分位 -> 1,234.50
    - {amount:>12,.2f}  右对齐占 12 列
    """
    return f"{currency} {amount:.2f}"


def convert_demo() -> None:
    """字符串与数字互转。注意 int('3.5') 会抛 ValueError。"""
    print(int("2026") + 1)        # 2027
    print(float("3.14") * 2)      # 6.28
    print(str(255) + "!")         # 255!

    # 练习：下面这行取消注释会怎样？为什么？
    # print(int("3.5"))


def main() -> None:
    print("--- 类型探测 ---")
    show_types()

    print("\n--- 金额格式化 ---")
    print(format_money(1234.5))
    print(format_money(1234.5, "USD"))

    print("\n--- 类型转换 ---")
    convert_demo()


if __name__ == "__main__":
    main()