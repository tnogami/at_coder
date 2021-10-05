S = input()
S1 = S[0:(len(S)-1)//2]
S2 = S[(len(S)-1)//2+1:]

if S==S[::-1] and S1==S1[::-1] and S2==S2[::-1]:
    print("Yes")
else:
    print("No")