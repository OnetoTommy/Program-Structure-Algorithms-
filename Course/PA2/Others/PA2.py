# ==========================
# Dynamic Programming - All Ways to Construct Target using Word Bank
#
# (1) Subproblem Definition:
#     ways(target): Return a list of all possible ways to construct the target string
#     by concatenating words from wordbank. Each way is represented as a list of words.
#
# (2) Decisions:
#     For each word in wordbank that matches the prefix of the target:
#         - Include this word in the current construction
#         - Recursively find all ways to construct the remaining suffix
#         - Combine this word with each way to construct the suffix
#
# (3) Recurrence Relation:
#     ways(target) = []  # Initialize empty list
#     For each word in wordbank:
#         If target starts with word:
#             suffix = target[len(word):]
#             suffix_ways = ways(suffix)  # Recursive call
#             target_ways = [word + each way in suffix_ways]
#             Add all target_ways to ways(target)
#     
#     Base case: ways("") = [[]]  # One way to construct empty string (using no words)
#
# (4) Memoization: Use a dictionary to cache results for target substrings
#
# (5) Print solution for each subproblem as it is computed
# ==========================

import argparse
import time
import sys

def all_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]  # base case: one way to construct empty string

    total_ways = []

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, wordbank, memo)
            target_ways = [[word] + way for way in suffix_ways]
            total_ways.extend(target_ways)

    memo[target] = total_ways

    print(f"Subproblem: '{target}' → {total_ways}")
    return total_ways

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True, help='Target string')
    parser.add_argument('--wordbank', required=True, help='Space-separated list of words')
    args = parser.parse_args()

    target = args.target
    wordbank = args.wordbank.split()

    if target is None:
        print("Error: Target string is required.")
        sys.exit(1)
    if not wordbank:
        print("Error: Wordbank cannot be empty.")
        sys.exit(1)

    start_time = time.time()
    result = all_construct(target, wordbank)
    end_time = time.time()

    print("\n=== All Ways to Construct Target ===")
    for way in result:
        print(way)

    print(f"\nRuntime: {end_time - start_time:.6f} seconds")

if __name__ == '__main__':
    main()