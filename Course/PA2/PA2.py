"""
INFO6205 - PA2

Subproblem Definition:
----------------------
We define a function `all_construct(target)` that returns all possible ways to construct the given
'target' string using the elements from the 'wordbank' list.

Each subproblem corresponds to a suffix of the original target string. The problem is broken down
by removing a prefix (a word from wordbank) and recursively solving for the remaining suffix.

Decisions:
----------
At each step, we iterate through the wordbank. If a word is a prefix of the current target,
we choose that word and recursively try to construct the remaining suffix. The overall
solution will be a combination of the chosen word and the solutions to the subproblem.

Recursion:
----------
all_construct(target) = [
    [word] + way
    for word in wordbank
    if target.startswith(word)
    for way in all_construct(target[len(word):])
]

Base Case:
----------
If the target is an empty string, we return `[[]]`, representing one valid way to construct nothing.
"""

import argparse
import time

def all_construct(target, wordbank, memo=None):
    """
     Recursively builds all possible ways to construct the target using words from the wordbank.

     Args:
         target (str): The target string to construct.
         wordbank (List[str]): List of words that can be used to construct the target.
         memo (dict): Memoization dictionary to store results of subproblems.

     Returns:
         List[List[str]]: A list of all combinations (as lists) that form the target.
     """
    if memo is None:
        memo = {}

    if target == "":
        return [[]]  # Base case: one valid way to construct nothing

    result = []

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]  # Remove prefix
            suffix_ways = all_construct(suffix, wordbank, memo)  # Recurse on suffix
            target_ways = [[word] + way for way in suffix_ways]  # Prepend current word
            result.extend(target_ways)  # Add all combinations to result

    memo[target] = result  # Save in memo before returning
    return result


def main():
    """
    Entry point for the program. Parses command-line arguments and prints results.
    """
    parser = argparse.ArgumentParser(description="Find all ways to construct a target from a wordbank.")
    parser.add_argument('-target', type=str, required=True, help="The target string to construct.")
    parser.add_argument('-wordbank', nargs='*', default=[], help="The list of words in the wordbank (optional).")
    args = parser.parse_args()

    target = args.target
    wordbank = args.wordbank

    start_time = time.time()
    ways = all_construct(target, wordbank)
    end_time = time.time()

    print(f"\nNumber of ways: {len(ways)}")
    print("[")
    for way in ways:
        print(f"  {way}")
    print("]")
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")


if __name__ == '__main__':
    main()
