"""CoinExchange"""
import json

def coin_exchange(amount=int, coins=dict):
    """coin"""
    i = 0
    coins_list = [(k,v) for k,v in coins.items()] 
    key_item = [int(k) for k,v in coins.items()]
    check = dict.fromkeys(key_item, 0)
    count, exchange = 0, False
    while amount > 0:
        index = coins_list[i][0]
        if coins[index] == 0:
            i += 1
        else:
            if amount - list(coins.keys())[i] >= 0:
                amount -= list(coins.keys())[i]
                coins[index] -= 1
                check[index] += 1
                count += 1
                exchange = True
            else:
                i += 1
        if i > len(key_item)-1:
            exchange = False
            break
    if exchange == False:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for a, b in check.items():
            print(f"  {a} baht = {b} coins")
        print(f"Number of coins: {count}")

def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    amount = int(input())
    data = convert_key(json.loads(input()))
    print(f"Amount: {amount}")
    coin_exchange(amount, data)
main()