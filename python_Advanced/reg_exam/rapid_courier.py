from collections import deque

package_weights = [int(p) for p in input().split()]
courier_capacities = deque(int(c) for c in input().split())

total_delivered_weight = 0

while package_weights and courier_capacities:
    current_package = package_weights[-1]
    current_courier = courier_capacities[0]

    if current_courier >= current_package:
        total_delivered_weight += current_package
        package_weights.pop()
        if current_courier > current_package:
            new_capacity = current_courier - 2 * current_package
            if new_capacity > 0:
                courier_capacities.append(new_capacity)
        courier_capacities.popleft()
    else:
        total_delivered_weight += current_courier
        package_weights[-1] -= current_courier
        courier_capacities.popleft()

print(f"Total weight: {total_delivered_weight} kg")

if not package_weights and not courier_capacities:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif package_weights and not courier_capacities:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, package_weights))}")
elif not package_weights and courier_capacities:
    print(f"Couriers are still on duty: {', '.join(map(str, courier_capacities))} but there are no more packages to deliver.")
