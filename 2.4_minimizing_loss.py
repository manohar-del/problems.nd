def m(p):
    l = float('inf')
    b = s = -1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[j] < p[i]:
                d = p[i] - p[j]
                if d < l:
                    l = d
                    b = i + 1
                    s = j + 1
    return (b, s, l if l != float('inf') else -1)

p = []

n = int(input("Enter the number of years: "))
for i in range(n):
    p.append(int(input(f"Enter loss for year {i + 1}: ")))

e = m(p)

print(f"price = {p}")
print("The year to buy:", e[0])
print("The year to sell:", e[1])
print("The loss:", e[2])
