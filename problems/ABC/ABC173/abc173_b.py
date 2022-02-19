import collections
d = collections.defaultdict(int)
N = int(input())
for _ in range(N):
    d[input()] += 1

print("AC x {}".format(d["AC"]))
print("WA x {}".format(d["WA"]))
print("TLE x {}".format(d["TLE"]))
print("RE x {}".format(d["RE"]))
