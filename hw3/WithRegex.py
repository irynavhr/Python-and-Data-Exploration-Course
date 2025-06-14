import re


file = open("cereals.csv")
lines = file.readlines()
file.close()


lines = lines[1:]


hot_cereals = []
cold_cereals = []

csv_pattern = re.compile(r'"([^"]*)"|([^,]+)')

# number_pattern = re.compile(r'^-?\d+(\.\d+)?$')

for line in lines:
    matches = csv_pattern.findall(line.strip())

    parts = []
    for m in matches:
        if m[0]:
            parts.append(m[0])
        else:
            parts.append(m[1])

    if len(parts) < 16:
        continue

    name = parts[0]
    cereal_type = parts[2].strip().upper()
    rating_str = parts[15].strip()

    # r'^-?\d+(\.\d*)?$'

    if not re.findall(r'^-?\d+(\.\d+)?$', rating_str):
        continue

    rating = float(rating_str)

    if cereal_type == "H":
        hot_cereals.append((rating, name))
    elif cereal_type == "C":
        cold_cereals.append((rating, name))


def calculate_average(cereal_list):
    total = 0
    count = 0

    for item in cereal_list:
        total += item[0]
        count += 1

    if count > 0:
        avg = total / count
        return avg
    else:
        return 0


if hot_cereals:
    min_hot = min(hot_cereals)
    max_hot = max(hot_cereals)
    avg_hot = calculate_average(hot_cereals)

    print(f"Cereal type: Hot")
    print(
        f"The lowest cereals rating value: {min_hot[0]} Cereal name: {min_hot[1]}")
    print(f"The average cereals rating value: {avg_hot:.2f}")
    print(
        f"The highest cereals rating value: {max_hot[0]} Cereal name: {max_hot[1]}\n")


if cold_cereals:
    min_cold = min(cold_cereals)
    max_cold = max(cold_cereals)
    avg_cold = calculate_average(cold_cereals)

    print(f"Cereal type: Cold")
    print(
        f"The lowest cereals rating value: {min_cold[0]} Cereal name: {min_cold[1]}")
    print(f"The average cereals rating value: {avg_cold:.2f}")
    print(
        f"The highest cereals rating value: {max_cold[0]} Cereal name: {max_cold[1]}\n")
