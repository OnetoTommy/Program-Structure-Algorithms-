def brute_force_coin_change(denominations, target_amount):
    # 生成所有可能的硬币组合
    min_coins = float('inf')

    # 外层循环，尝试不同数量的 25 面值硬币
    for x in range(target_amount // denominations[0] + 1):
        # 中层循环，尝试不同数量的 10 面值硬币
        for y in range((target_amount - x * denominations[0]) // denominations[1] + 1):
            # 内层循环，尝试不同数量的 1 面值硬币
            for z in range((target_amount - x * denominations[0] - y * denominations[1]) // denominations[2] + 1):
                # 计算当前组合的总金额
                total_amount = x * denominations[0] + y * denominations[1] + z * denominations[2]
                # 如果总金额等于目标金额，则更新最小硬币数
                if total_amount == target_amount:
                    min_coins = min(min_coins, x + y + z)

    return min_coins


# Example #2: Denominations S = {25, 10, 1}, Target Amount N = 40
denominations = [25, 10, 1]
target_amount = 40

min_coins_needed = brute_force_coin_change(denominations, target_amount)
print(f"The minimum number of coins needed to make {target_amount} is: {min_coins_needed}")
