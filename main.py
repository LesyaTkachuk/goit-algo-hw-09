from timeit import timeit

from constants import COINS
from find_min_coins_amount_greedy import find_min_coins_amount_greedy
from find_min_coins_amount_dynamic import find_min_coins_amount_dynamic


def main():
    change_17 = 17
    change_68 = 68

    # greedy algorithm solving approach
    greedy_find_min_coins_for_17_time = timeit(
        lambda: find_min_coins_amount_greedy(COINS, change_17), number=3
    )
    greedy_find_min_coins_for_68_time = timeit(
        lambda: find_min_coins_amount_greedy(COINS, change_68), number=3
    )

    # dynamic programming solving approach
    dynamic_find_min_coins_for_17_time = timeit(
        lambda: find_min_coins_amount_dynamic(COINS, change_17), number=3
    )
    dynamic_find_min_coins_for_68_time = timeit(
        lambda: find_min_coins_amount_dynamic(COINS, change_68), number=3
    )

    print("-" * 70)
    print(f"{'Aproach':<20} | {'Time for 17':<23} | {'Time for 68':<20}")
    print("-" * 70)
    print(
        f"{'Greedy Algorithm':<20} | {greedy_find_min_coins_for_17_time:<23} | {greedy_find_min_coins_for_68_time:<20}"
    )
    print("-" * 70)
    print(
        f"{'Dynamic programming':<20} | {dynamic_find_min_coins_for_17_time:<23} | {dynamic_find_min_coins_for_68_time:<20}"
    )
    print("-" * 70)
    print(
        f"Greedy approach is in {dynamic_find_min_coins_for_17_time//greedy_find_min_coins_for_17_time} times faster than dynamic programming one for 17 change amount"
    )
    print(
        f"Greedy approach is in {dynamic_find_min_coins_for_68_time//greedy_find_min_coins_for_68_time} times faster than dynamic programming one for 68 change amount"
    )


if __name__ == "__main__":
    main()
