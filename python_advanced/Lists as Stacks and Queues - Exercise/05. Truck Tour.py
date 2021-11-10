from collections import deque

count_pumps = int(input())

pumps = deque(
    [
        [int(i) for i in input().split()]
        for _ in range(count_pumps)
    ]
)

for pump in range(count_pumps):

    is_valid = True
    fuel = 0
    for _ in range(count_pumps):
        current = pumps.popleft()
        fuel += current[0] - current[1]

        if fuel < 0:
            is_valid = False

        pumps.append(current)

    if is_valid:
        print(pump)
        break

    pumps.append(pumps.popleft())
