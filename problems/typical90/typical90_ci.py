d = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
al = ["M", "D", "C", "L", "X", "V", "I"]
ans = dict()
ret = 0
for n in range(10, 4000):
    ans = ""
    for a in al:
        while 0<n-d[a]:
            ans += a
            n -= d[a]
            
    if len(ans) == 8 and not("IIII" in ans or "XXXX" in ans or "CCCC"):
        ret += n
            
ret