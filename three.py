import sys
number = int(sys.stdin.read().strip())

if number < pow(10,3):
    half = number // 2

    l3 = list(range(0,half,3))

    l5 = list(range(0,half,5))

    differ = list(range(0,half,15))

    total = sum(l3) + sum(l5) - sum(differ)

    l3 = list(range(half,number,3))

    l5 = list(range(half,number,5))

    differ = list(range(half,number,15))

    total += sum(l3) + sum(l5) - sum(differ)
else:
    l3 = list(range(0,number,3))

    l5 = list(range(0,number,5))

    differ = list(range(0,number,15))

    total = sum(l3) + sum(l5) - sum(differ)

print(total)