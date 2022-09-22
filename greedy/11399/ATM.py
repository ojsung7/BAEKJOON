len = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

result = 0

for i in range(0, len):
  result += num_list[i]
  for j in range(0,i):
    result += num_list[j]

print(result)