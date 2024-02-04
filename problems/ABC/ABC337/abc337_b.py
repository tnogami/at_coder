S = input()

while 'AA' in S:
    S = S.replace('AA', 'A')
while 'BB' in S:
    S = S.replace('BB', 'B')
while 'CC' in S:
    S = S.replace('CC', 'C')

if S == 'ABC' or S == 'A' or S == 'B' or S == 'C' or S == '' or S == 'AB' or S == 'BC' or S == 'AC':
    print('Yes')
else:
    print('No')