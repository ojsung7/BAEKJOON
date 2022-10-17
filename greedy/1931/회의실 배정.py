import sys

N = int(sys.stdin.readline())

ary = [[0] * 2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    ary[i][0] = s
    ary[i][1] = e

ary.sort(key=lambda x: x[0])
ary.sort(key=lambda x: x[1])
count = 0

check = ary[0][0]

for line in ary:
    if check <= line[0]:
        count += 1
        check = line[1]

print(count)