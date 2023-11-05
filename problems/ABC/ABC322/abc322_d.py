def solve(E1, E2, E3):
    from copy import deepcopy

    for i1 in range(-2, 3):
        for j1 in range(-2, 3):
            for i2 in range(-2, 3):
                for j2 in range(-2, 3):
                    for i3 in range(-2, 3):
                        for j3 in range(-2, 3):
                            flag = False
                            field = [[False]*4 for _ in range(4)]
                            for k, e1 in enumerate(E1):
                                for l, e in enumerate(e1):
                                    if e == "#":
                                        if k + i1 < 0 or 4 <= k+i1 or l + j1 < 0 or 4 <= l+j1:
                                            flag = True
                                            break
                                        elif field[k+i1][l+j1] == True:
                                            flag = True
                                            break
                                        else:
                                            field[k+i1][l+j1] = True

                            if flag:
                                continue

                            for k, e2 in enumerate(E2):
                                for l, e in enumerate(e2):
                                    if e == "#":
                                        if k + i2 < 0 or 4 <= k+i2 or l + j2 < 0 or 4 <= l+j2:
                                            flag = True
                                            break
                                        elif field[k+i2][l+j2] == True:
                                            flag = True
                                            break
                                        else:
                                            field[k+i2][l+j2] = True

                            if flag:
                                continue

                            for k, e3 in enumerate(E3):
                                for l, e in enumerate(e3):
                                    if e == "#":
                                        if k + i3 < 0 or 4 <= k+i3 or l + j3 < 0 or 4 <= l+j3:
                                            flag = True
                                            break
                                        elif field[k+i3][l+j3] == True:
                                            flag = True
                                            break
                                        else:
                                            field[k+i3][l+j3] = True

                            if flag:
                                continue

                            check = True
                            for ff in field:
                                for f in ff:
                                    if f == False:
                                        check = False

                            if check:
                                return True
                            else:
                                continue

    return False


P1 = [input() for _ in range(4)]
P2 = [input() for _ in range(4)]
P3 = [input() for _ in range(4)]


for i in range(4):
    P1 = list(zip(*reversed(P1)))
    for j in range(4):
        P2 = list(zip(*reversed(P2)))
        for k in range(4):
            P3 = list(zip(*reversed(P3)))
            if solve(P1, P2, P3):
                print("Yes")
                exit()

print('No')
