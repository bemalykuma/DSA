class Item:
    def __init__(self, name, price=int, weight=float):
        self.name = name
        self.price = price
        self.weight = weight
    
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_weight(self):
        return self.weight
    def get_cost(self):
        return self.price / self.weight
    
def knapsack(amount, itemList):
    total, i, kg = 0, 0, 0
    cost, all_item = [], []
    for j in range(len(itemList)):
        cost.append(itemList[j].get_cost())
        all_item.append((itemList[j].get_cost(), itemList[j]))
    sort_list = sorted(all_item, key=lambda x:x[0], reverse=True)
    print(f"Knapsack Size: {amount} kg") 
    print("===============================")
    while kg <= amount:
        obj = sort_list[i][1]
        kg += obj.get_weight()
        if kg > amount:
            break
        total += obj.get_price()
        print(f"{obj.get_name()} -> {obj.get_weight()} kg -> {obj.get_price()} THB")
        i += 1
        if i >= len(itemList):
            break
        elif (kg + sort_list[i][1].get_weight()) > amount:
            break
    print(f"Total: {total} THB")


def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)
main()