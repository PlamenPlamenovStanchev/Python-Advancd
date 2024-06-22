def choose_coins(coins, target):
    coins.sort(reversed=True)
    used_coins = {}

    index = 0
    while target != 0 and index < len(coins):
        count_coins = target // coins[index]
        target %= coins[index]

        if count_coins > 0:
            used_coins[coins[index]] = count_coins

        index += 1

    if target != 0:
        return 'Error'

    result = f"Number of coins to take: {sum(used_coins.values())}\n"
    for value, count in used_coins.items():
        result += f"{count} coin(s) with value {value}\n"

    return result.strip()


coins_list = [int(x) for x in input().split(', ')]
target_sum = int(input())
print(choose_coins(coins_list, target_sum))

