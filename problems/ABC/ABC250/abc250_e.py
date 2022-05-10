N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = int(input())

hash1 = []
hash2 = []

set1 = set()
set2 = set()

sum1 = 0
for a in A:
    hash_a = a*(a+1346)*(a+9185)
    if hash_a in set1:
        hash1.append(sum1)
    else:
        hash1.append(sum1+hash_a)
        sum1 += hash_a
        set1.add(hash_a)

sum2 = 0
for b in B:
    hash_b = b*(b+1346)*(b+9185)
    if hash_b in set2:
        hash2.append(sum2)
    else:
        hash2.append(sum2+hash_b)
        sum2 += hash_b
        set2.add(hash_b)

for q in range(Q):
    x1, x2 = map(int, input().split())
    if hash1[x1-1] == hash2[x2-1]:
        print("Yes")
    else:
        print("No")

