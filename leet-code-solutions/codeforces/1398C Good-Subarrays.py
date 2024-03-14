from collections import defaultdict
tcase = int(input())
for i in range(tcase):
    length = int(input())
    nums = list(input())
    map = defaultdict(int)
    
    prefix = []
    total = 0
    for i in nums:
        prefix.append(total)
        total += int(i)
    prefix.append(total)

    count = 0
    for i in range(len(prefix)):
        count += map[prefix[i] - i]
        map[prefix[i] - i] += 1

    print(count)