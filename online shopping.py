d = {}
n = int(input())
for i in range(n):
    line = input().split()
    if line[0] not in d:
        d[line[0]] = d.setdefault(line[0], {})
        if line[1] not in d[line[0]]:
            x = int(line[2])
            d[line[0]][line[1]] = d[line[0]].setdefault(line[1], x)
    else:
        if line[1] not in d[line[0]]:
            x = int(line[2])
            d[line[0]][line[1]] = d[line[0]].setdefault(line[1], x)
        else:
            x = int(line[2])
            d[line[0]][line[1]] += x
for key in sorted(d):
    print(key+':')
    for key1 in sorted(d[key]):
        print(key1, d[key][key1])