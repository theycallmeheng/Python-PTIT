t = int(input())
mapping = {'0' : '0', '1' : '1', '8' : '0', '9' : '0'}

for _ in range(t):
    s = input().strip()
    res = []
    valid = True
    for ch in s:
        if ch not in mapping:
            valid = False
            break
        res.append(mapping[ch])
        
    if not valid:
        print("INVALID")
    else:
        ans = "".join(res).lstrip("0")
        print(ans if ans else "INVALID")