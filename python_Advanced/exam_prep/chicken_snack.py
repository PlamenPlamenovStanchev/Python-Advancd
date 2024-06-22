from collections import deque


money = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])
food_count = 0

while money and food_prices:
    if money[-1] == food_prices[0]:
        food_count += 1
        money.pop()
        food_prices.popleft()

    elif money[-1] > food_prices[0]:
        difference = money.pop() - food_prices.popleft()
        food_count += 1
        if not money:
            money =[difference]
        else:
            money[-1] += difference

    else:
        money.pop()
        food_prices.popleft()


if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 1 < food_count < 4:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food")
else:
    print(f"Henry remained hungry. He will try next weekend again.")



