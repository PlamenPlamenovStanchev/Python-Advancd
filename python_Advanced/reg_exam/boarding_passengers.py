# def boarding_passengers(ship_capacity, *args):
#     boarded_passengers = {}
#     available_capacity = ship_capacity
#
#     for group in args:
#         number_of_passengers, benefits_program = group
#         if number_of_passengers <= available_capacity:
#             if benefits_program in boarded_passengers:
#                 boarded_passengers[benefits_program] += number_of_passengers
#             else:
#                 boarded_passengers[benefits_program] = number_of_passengers
#             available_capacity -= number_of_passengers
#
#     sorted_boarded_passengers = sorted(boarded_passengers.items(), key=lambda x: (-x[1], x[0]))
#     result = []
#     for program, count in sorted_boarded_passengers:
#         result.append(f"## {program}: {count} guests")
#
#     if available_capacity == 0:
#         if len(args) == sum(len(str(v)) for v in boarded_passengers.values()):
#             result.append("All passengers are successfully boarded!")
#         else:
#             result.append("Boarding unsuccessful. Cruise ship at full capacity.")
#     else:
#         result.append(f"Partial boarding completed. Available capacity: {available_capacity}.")
#
#     return "\n".join(result)
#
#
def boarding_passengers(capacity, *args):
    benefit_programs = {}
    available_capacity = capacity

    for group in args:
        passengers, benefit_program = group
        if available_capacity >= passengers:
            available_capacity -= passengers
            if benefit_program in benefit_programs:
                benefit_programs[benefit_program] += passengers
            else:
                benefit_programs[benefit_program] = passengers
        else:
            continue

    if available_capacity == 0:
        if available_capacity == capacity:
            message = "All passengers are successfully boarded!"
        else:
            message = "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        message = f"Partial boarding completed. Available capacity: {available_capacity}."

    boarding_details = "Boarding details by benefit plan:\n"
    for program, count in sorted(benefit_programs.items(), key=lambda x: (-x[1], x[0])):
        boarding_details += f"## {program}: {count} guests\n"

    return boarding_details + message



# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))