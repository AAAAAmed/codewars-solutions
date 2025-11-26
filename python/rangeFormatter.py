# Kata: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
def solution(args):
    lists = [[]]
    lists[0].append(args.pop(0))
    for num in args:
        if num - 1 != lists[-1][-1]:
            lists.append([])
        lists[-1].append(num)

    output = ''
    for l in lists:
        if len(l) < 3:
            for num in l:
                output += f"{num},"
        else:
            output += f"{l[0]}-{l[-1]},"

    return output[:-1]

print(solution([0, 1, 2, 3, 5, 6, 8, 10]))
print('Expected: 0-3,5,6,8,10')
