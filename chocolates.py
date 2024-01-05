def buyChoco(prices, money):
    sorted_prices = sorted(prices)
    two_choco = sorted_prices[0] + sorted_prices[1]
    if money - two_choco >= 0:
        money = money - two_choco
        print(f"if {money}")
    else:
        print(f"else {money}")



buyChoco([1, 2, 2,], 3)    
        