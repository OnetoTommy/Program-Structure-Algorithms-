import time
import argparse

# (1) Subproblem definition and recurrence explained above

def all_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, wordbank, memo)
            target_ways = [ [word] + way for way in suffix_ways ]
            result.extend(target_ways)

    memo[target] = result
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', type=str, required=True)
    parser.add_argument('--wordbank', nargs='+', required=True)
    args = parser.parse_args()

    target = args.target
    wordbank = args.wordbank

    start_time = time.time()
    ways = all_construct(target, wordbank)
    end_time = time.time()

    print(f"Number of ways: {len(ways)}")
    print("[")
    for way in ways:
        print(f"  {way}")
    print("]")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
