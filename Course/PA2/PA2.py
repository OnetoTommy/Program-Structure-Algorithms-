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
import sys

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

    if target in memo:  # If target is already computed, return the cached result
        return memo[target]

    result = []

    # Iterate through the wordbank to check for prefix matches
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]  # Remove the prefix (word)
            suffix_ways = all_construct(suffix, wordbank, memo)  # Recursively solve for the suffix
            target_ways = [[word] + way for way in suffix_ways]  # Prepend current word to each solution
            result.extend(target_ways)  # Add all combinations to the result

    memo[target] = result  # Save the result in memo before returning

    print(f"Subproblem: '{target}' → {result}")
    return result


def main():
    """
    Entry point for the program. Parses command-line arguments and prints results.
    """
    parser = argparse.ArgumentParser(description="Find all ways to construct a target from a wordbank.")
    parser.add_argument('-target', type=str, required=True, help="The target string to construct.")
    parser.add_argument('-wordbank', nargs='*', default=[], help="The list of words in the wordbank (optional).")
    args = parser.parse_args()

    # If wordbank is explicitly provided as an empty string, treat it as an empty list
    if args.wordbank == ['']:
        args.wordbank = []

    # Join raw input to check for malformed syntax
    raw_args = " ".join(sys.argv)

    # Warnings for possible missing spaces near -target or -wordbank
    if "-target" in raw_args and not " -target " in raw_args:
        print("Warning: Missing space before or after -target. Did you mean `-target yourstring`?")
    if "-wordbank" in raw_args and not " -wordbank " in raw_args:
        print("Warning: Missing space before or after -wordbank. Did you mean `-wordbank word1 word2 ...`?")

    # Validate the target
    target = args.target
    if not isinstance(target, str):
        print("Error: Invalid format for target string.")
        return

    # Validate wordbank is a list of strings
    wordbank = args.wordbank
    if not isinstance(wordbank, list) or not all(isinstance(word, str) for word in wordbank):
        print("Error: Wordbank must be a list of strings.")
        return

    # Base case: If wordbank is empty and target is not empty, return empty list
    if not wordbank and target != "":
        print("Error: Wordbank is empty.")
        return

    # Timing the solution process
    start_time = time.time()
    ways = all_construct(target, wordbank)
    end_time = time.time()

    # Print the results
    print(f"\nNumber of ways: {len(ways)}")
    print("[")
    for way in ways:
        formatted_way = [f"\"{word}\"" for word in way]
        print(f"[ {', '.join(formatted_way)} ]")
    print("]")
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")


if __name__ == '__main__':
    main()
