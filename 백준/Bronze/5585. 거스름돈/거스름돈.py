money = 1000 - int(input())

coin = 0
while money > 0:
    if money >= 500:
        coin += money // 500
        money = money % 500
    elif money >= 100:
        coin += money // 100
        money = money % 100
    elif money >= 50:
        coin += money // 50
        money = money % 50
    elif money >= 10:
        coin += money // 10
        money = money % 10
    elif money >= 5:
        coin += money // 5
        money = money % 5
    else:
        coin += money
        break
    
print(coin)