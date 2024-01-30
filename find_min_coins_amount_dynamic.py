from constants import COINS


def find_min_coins_amount_dynamic(coins, change):
    # min number of coins required for the change amount that is equal to the index
    min_coins_required = [0] + [float("inf")] * change
    # max coin required for the change amount that is equal to the index
    max_coin_required = [0] * (change + 1)

    # fill both tables based on calculations
    for amount in range(1, change + 1):
        for coin in sorted(coins, reverse=True):
            if (
                amount >= coin
                and min_coins_required[amount - coin] + 1 < min_coins_required[amount]
            ):
                min_coins_required[amount] = min_coins_required[amount - coin] + 1
                max_coin_required[amount] = coin

    coins_amount = {}
    current_sum = change

    # find coins amount using both tables
    while current_sum > 0:
        coin = max_coin_required[current_sum]
        coins_amount[coin] = coins_amount.get(coin, 0) + 1
        current_sum -= coin

    return coins_amount


if __name__ == "__main__":
    result_15 = find_min_coins_amount_dynamic(COINS, 15)
    print("Coins amount for 15 (dynamic): ", result_15)  # {10: 1, 5: 1}

    result_167 = find_min_coins_amount_dynamic(COINS, 167)
    print("Coins amount for 167 (dynamic): ", result_167)  # {50: 1, 10: 1, 5: 1, 2: 1}
