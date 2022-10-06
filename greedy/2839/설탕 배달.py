import math

result = -1

kg = int(input())

for_range = math.trunc(kg / 3)
check_3 = False

if kg >= 5:
    if kg % 5 == 0:
        result = math.trunc(kg / 5)
    else:
        for index_5 in range(for_range, 0, -1):
            for index_3 in range(for_range, 0, -1):
                if (index_3 * 3) + (index_5 * 5) == kg:
                    result = int(index_3) + int(index_5)
                    check_3 = True
                    break
            if check_3:
                break

if result == -1 and kg % 3 == 0:
    result = math.trunc(kg / 3)

print(result)