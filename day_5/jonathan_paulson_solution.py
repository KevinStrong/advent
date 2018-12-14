s = open('full_polymer.txt').read().strip()

alpha = 'abcdefghijklmnopqrstuvwxyz'
M = {}
for c in alpha:
    M[c.lower()] = c.upper()
    M[c.upper()] = c.lower()

ans = 1e5
for rem in alpha:
    s2 = [c for c in s if c != rem.lower() and c != rem.upper()]
    stack = []
    for c in s2:
        if stack and c == M[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    ans = min(ans, len(stack))
    print(rem + ": " + str(len(stack)))
print(ans)
