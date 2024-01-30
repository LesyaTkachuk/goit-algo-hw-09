from constants import COINS


def find_min_coins_amount_greedy(coins, change_amount):
    coins_amount = {}

    for coin in sorted(coins, reverse=True):
        if change_amount <= 0:
            return coins_amount

        amount = change_amount // coin
        if amount > 0:
            coins_amount[coin] = amount
            change_amount -= coin * amount
    return coins_amount


if __name__ == "__main__":
    result_15 = find_min_coins_amount_greedy(COINS, 15)
    print("Coins amount for 15 (greedy): ", result_15)  # {10: 1, 5: 1}

    result_167 = find_min_coins_amount_greedy(COINS, 167)
    print("Coins amount for 167 (greedy): ", result_167)  # {50: 1, 10: 1, 5: 1, 2: 1}
