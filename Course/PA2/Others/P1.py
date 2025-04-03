import time
import argparse

def solution(target, wordbank, memo = None):

    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []
    for word in wordbank:
        if target.startswith(word):
            suffix = word[len(word):]
            suffix_way = solution(suffix, wordbank, memo)
            target_way = [[word + way for way in suffix_way]]
            result.extend(target_way)
    memo[target] = result
    return result