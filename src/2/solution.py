def safe_levels(levels: list):
    is_increasing = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        if is_increasing and (
            levels[i] >= levels[i + 1] or abs(levels[i] - levels[i + 1]) > 3
        ):
            return False
        elif not is_increasing and (
            levels[i] <= levels[i + 1] or abs(levels[i] - levels[i + 1]) > 3
        ):
            return False
    return True


with open("./input.txt", "r") as file:
    p1, p2 = 0, 0
    for line in file.readlines():
        levels = line.strip().split(" ")
        levels = [int(level) for level in levels]
        if safe_levels(levels):
            p1 += 1

        is_good = False
        for j in range(len(levels)):
            modified_levels = levels[:j] + levels[j + 1 :]
            if safe_levels(modified_levels):
                is_good = True
                break
        if is_good:
            p2 += 1

print(p1)
print(p2)
