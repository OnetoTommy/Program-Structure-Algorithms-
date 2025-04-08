import argparse
import time

def all_construct(target, wordbank, memo=None):
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
