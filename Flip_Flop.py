def flipflop(t):
    L_index = len(t)-1
    F_index = 0
    while F_index < L_index :
        if t[F_index] != t[L_index] :
            return False
        F_index +=1
        L_index -=1
    return True

truple = (3,4,5,5,4,3,8)

if flipflop(truple):
    print("Truple is flip flop")

else:
    print("Truple is not flip flop")