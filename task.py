coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum):
    res = {}
    for coin in coins:
        coinCount = sum // coin
        if coinCount:
          sum -= coinCount * coin
          res[coin] = coinCount
    return res

def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_count = [{} for _ in range(amount + 1)]
    coin_count[0] = {coin: 0 for coin in coins}

    for sub_amount in range(1, amount + 1):
        for coin in coins:
            if sub_amount >= coin:
                if min_coins[sub_amount - coin] + 1 < min_coins[sub_amount]:
                    min_coins[sub_amount] = min_coins[sub_amount - coin] + 1
                    coin_count[sub_amount] = coin_count[sub_amount - coin].copy()
                    if coin in coin_count[sub_amount]:
                        coin_count[sub_amount][coin] += 1
                    else:
                        coin_count[sub_amount][coin] = 1
 
    final_count = {coin: count for coin, count in coin_count[amount].items() if count > 0}

    return final_count

print('Результат алгоритму динамічного програмування: ')
print(find_min_coins(113))  # Виведе: {50: 2, 10: 1, 2: 1, 1: 1}
print('Результат жадібного алгоритму: ')
print(find_coins_greedy(113))