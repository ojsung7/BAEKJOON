first_in = list(map(int, input().split()))

coins = list()

for i in range(first_in[0]):
    coins.append(int(input()))

coin_count = 0

for i in reversed(range(len(coins))):
    coin_count += first_in[1] // coins[i]
    first_in[1] %= coins[i]

print(coin_count)