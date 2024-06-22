from collections import deque


contestants = deque(int(c) for c in input().split())
pies = [int(p) for p in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()

    if contestant >= pie:
        contestant -= pie

        if contestant > 0:
            contestants.append(contestant)

    else:
        pie -= contestant

        if pies and pie == 1:
            pies[-1] += pie
        else:
            pies.append(pie)

if not pies and not contestants:
    print('We have a champion')
elif contestants:
    print("We will have for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(c) for c in contestants)}")
elif pies:
    print("Our contestant need to rest")
    print(f" Pies left: {', '.join(str(p) for p in pies)}")
