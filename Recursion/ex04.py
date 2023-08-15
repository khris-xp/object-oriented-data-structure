def perket(lst, sour=1, bitter=0, path=[]):
    if not lst:
        p = len(path) if not any(path) else 0
        return abs(sour - bitter) * 10 ** p
    return min(perket(lst[1:], sour*lst[0][0], bitter+lst[0][1], path+[True]), perket(lst[1:], sour, bitter, path+[False]))

def recursive_split(lst: 'list[str]'):
    if not lst:
        return []
    a,b = lst[0].split()
    return [[int(a), int(b)]] + recursive_split(lst[1:])

inp = recursive_split(input("Enter Input : ").split(","))

print(perket(inp))