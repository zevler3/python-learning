# Python Learning

记录我的 Python 学习过程：代码练习、笔记、踩坑记录。

## 环境

- Python 3.x（`python --version` 查看）
- Windows 11
- Git for Windows 2.45.1
- 编辑器：VS Code

## 学习进度

- [x] 环境搭建：Python + Git + 虚拟环境
- [x] 基础语法：变量、类型、控制流
- [x] 数据结构：list / dict / set / tuple
- [ ] 函数与作用域
- [ ] 面向对象
- [ ] 文件与异常
- [ ] 标准库：pathlib、json、csv
- [ ] 小项目：命令行 Todo

## 目录说明

| 目录 | 内容 |
|---|---|
| `Python-learning/01_basics` | 基础语法练习 |
| `Python-learning/02_functions` | 函数、作用域、参数 |
| `Python-learning/03_oop` | 类与对象 |
| `Python-learning/04_stdlib` | 标准库：文件 IO、json、csv、pathlib |
| `Python-learning/05_venv_pip` | 虚拟环境与依赖管理笔记 |
| `projects/` | 小项目 |
| `计算机作业/` | 课程作业练习 |

## 踩坑记录

- `list.append()` 返回 `None`，不是新列表
- 可变默认参数 `def f(x=[])` 会跨调用累积，改用 `None` 再判空
- Windows 上读写文件显式指定 `encoding="utf-8"`，避免 GBK 解码报错
- 提交前一定先 `git status`，别把 `.venv` 加进去

## 如何运行

```powershell
python "Python-learning/01_basics/你的练习.py"
```

## 如何重建环境

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
