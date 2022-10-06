line = int(input())

asc = list(map(int, input().split()))
desc = list(map(int, input().split()))

result = 0

asc.sort()
desc.sort(reverse=True)

for i in range(0, line):
    result += asc[i] * desc[i]

print(result)