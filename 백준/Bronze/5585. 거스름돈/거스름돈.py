money = 1000 - int(input())
coins = [500, 100, 50, 10, 5]
cnt = 0

for coin in coins:
    cnt += money // coin
    money = money % coin
    
print(cnt + money)