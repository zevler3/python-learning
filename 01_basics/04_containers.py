"""01_basics · 常用容器

运行：python 04_containers.py

学习要点：
1. list 有序可变，dict 键值映射，set 去重无序，tuple 不可变。
2. 切片 lst[a:b] 含头不含尾，负数从末尾数。
3. 解包 a, b = b, a 是 Python 交换变量的惯用法。
"""


def list_basics() -> None:
    fruits = ["apple", "banana", "cherry", "date"]
    print(fruits[0], fruits[-1])      # apple date
    print(fruits[1:3])                # ['banana', 'cherry']
    print(fruits[::-1])               # 反转

    fruits.append("elderberry")
    fruits.remove("banana")
    print(sorted(fruits))


def dict_basics() -> None:
    scores = {"math": 92, "english": 85, "python": 98}

    for subject, score in scores.items():
        print(f"{subject:<10} {score:>3}")

    # 用 get 取可能不存在的键，避免 KeyError
    print(scores.get("history", "无记录"))
    print(f"平均分: {sum(scores.values()) / len(scores):.1f}")


def set_basics() -> None:
    # 去重 + 集合运算
    a = {"apple", "banana", "cherry"}
    b = {"banana", "date"}
    print(a & b)      # 交集 {'banana'}
    print(a | b)      # 并集
    print(a - b)      # 差集

    words = ["a", "b", "a", "c", "b"]
    print(set(words)) # 去重后顺序不保证


def tuple_unpack() -> None:
    point = (3, 5)
    x, y = point
    print(x, y)

    a, b = 1, 2
    a, b = b, a          # 交换，不需要中间变量
    print(a, b)

    # 函数返回多个值，本质是返回元组
    def min_max(nums: list[int]) -> tuple[int, int]:
        return min(nums), max(nums)

    low, high = min_max([4, 1, 9, 3])
    print(low, high)


def main() -> None:
    print("--- list ---");    list_basics()
    print("\n--- dict ---");  dict_basics()
    print("\n--- set ---");   set_basics()
    print("\n--- tuple ---"); tuple_unpack()


if __name__ == "__main__":
    main()