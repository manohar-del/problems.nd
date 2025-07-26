def o(p1, p2):
    l1, r1 = p1
    l2, r2 = p2
    x = max(0, min(r1, r2) - max(l1, l2))
    return x / (r1 - l1) > 0.5 or x / (r2 - l2) > 0.5

def c(a, b):
    r = []
    v = [0] * len(b)
    for i in a:
        f = 0
        for j, x in enumerate(b):
            if not v[j] and o(i['positions'], x['positions']):
                r.append({'positions': i['positions'], 'values': i['values'] + x['values']})
                v[j] = 1
                f = 1
                break
        if not f:
            r.append(i)
    for j, x in enumerate(b):
        if not v[j]:
            r.append(x)
    return sorted(r, key=lambda z: z['positions'][0])

def get_input_list(name):
    n = int(input(f"Enter number of segments in list {name}: "))
    segments = []
    for i in range(n):
        print(f"\nSegment {i+1} of {name}:")
        l = int(input("  Start position: "))
        r = int(input("  End position: "))
        vals = list(map(int, input("  Enter values (space-separated): ").split()))
        segments.append({'positions': [l, r], 'values': vals})
    return segments

a = get_input_list('A')
b = get_input_list('B')

print("\nMerged Output:")
print(c(a, b))
