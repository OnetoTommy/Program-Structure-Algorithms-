def coin_change(n):

    dict = {coin:0 for coin in range(3)}
    # return dict
    if n == 0:
        return dict

    while n > 0:
        if n >= 10:
            dict[2] += 1
            n -= 10
        elif n >= 6:
            dict[1] += 1
            n -= 6
        elif n >= 1:
            dict[0] += 1
            n -= 1
    return dict

coin_nums = coin_change(7)
min_coins = 0
for i in coin_nums:
    min_coins += coin_nums[i]
print(min_coins)