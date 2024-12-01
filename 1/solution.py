with open("./input.txt", "r") as file:
    left_list, right_list = [], []
    for line in file.readlines():
        left, right = line.split("   ")
        left_list.append(int(left.strip()))
        right_list.append(int(right.strip()))

left_list.sort()
right_list.sort()
distances = 0
for left, right in zip(left_list, right_list):
    distances += max(left, right) - min(left, right)

print(distances)

total_count = 0
for left in left_list:
    left_count = 0
    for right in right_list:
        if left == right:
            left_count += 1
    total_count += left * left_count


print(total_count)
