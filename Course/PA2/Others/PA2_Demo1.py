""" INFO6205 - PA2
Subproblem Definition:
----------------------
子问题定义为每个后缀字符串的可能构造方式，函数all_construct(target)返回构造目标字符串的所有可能组合。
递归过程中，每次尝试使用wordbank中的单词作为前缀，递归处理剩余后缀。

Decisions:
----------
每次选择wordbank中可作为当前target前缀的单词，递归处理剩余部分，将所有可能的组合合并。

Recursion:
----------
all_construct(target) = [ [word] + way for word in wordbank if target以word开头 for way in all_construct(剩余部分) ]

Base Case:
----------
当target为空字符串时，返回包含一个空列表的列表[[]]，表示一种有效构造方式（构造空字符串）。
"""
import argparse
import time
import sys


def all_construct(target, wordbank, memo=None):
    """
    递归计算所有构造目标字符串的方式，使用memoization优化重复子问题。

    Args:
        target (str): 要构造的目标字符串
        wordbank (list): 可用的单词列表（已去重且无空字符串）
        memo (dict): 记忆化存储字典

    Returns:
        list: 所有可能的构造方式列表，每个方式是一个单词列表
    """
    if memo is None:
        memo = {}

    # 基本情况：目标字符串为空，返回包含空组合的列表
    if target == "":
        return [[]]

    # 如果当前target已计算过，直接返回缓存结果
    if target in memo:
        return memo[target]

    result = []
    for word in wordbank:
        # 如果当前单词是目标字符串的前缀
        if target.startswith(word):
            suffix = target[len(word):]  # 剩余部分
            # 递归计算剩余部分的构造方式
            suffix_ways = all_construct(suffix, wordbank, memo)
            # 将当前单词添加到所有子组合的前面
            for way in suffix_ways:
                new_way = [word] + way
                result.append(new_way)

    # 将结果存入memo并打印子问题解（作业要求第5点）
    memo[target] = result
    print(f"Subproblem: '{target}' → {result}")  # 修正点：添加执行过程打印
    return result


def main():
    """处理命令行参数并输出结果"""
    # 参数解析
    parser = argparse.ArgumentParser(description="构造目标字符串的所有方式")
    parser.add_argument('-target', type=str, required=True, help="目标字符串")
    parser.add_argument('-wordbank', nargs='*', default=[], help="单词库列表")
    args = parser.parse_args()

    # 参数验证和预处理
    # 修正点：处理空字符串和重复单词
    # 1. 过滤空字符串并保留顺序去重
    wordbank = []
    seen = set()
    for word in args.wordbank:
        if word != "":  # 过滤空字符串
            if word not in seen:
                seen.add(word)
                wordbank.append(word)

    # 2. 输入验证
    if not isinstance(args.target, str):
        print("错误：目标字符串格式无效")
        return

    # 计时和执行核心逻辑
    start_time = time.time()
    ways = all_construct(args.target, wordbank)
    end_time = time.time()

    # 结果格式化输出
    print(f"\n方式数量: {len(ways)}")
    # 修正点：正确处理空结果输出格式
    if len(ways) == 0:
        print("[]")
    else:
        print("[")
        for way in ways:
            formatted = [f'"{w}"' for w in way]
            print(f"  [ {', '.join(formatted)} ],")
        print("]")
    print(f"耗时: {end_time - start_time:.6f} 秒")


if __name__ == '__main__':
    main()