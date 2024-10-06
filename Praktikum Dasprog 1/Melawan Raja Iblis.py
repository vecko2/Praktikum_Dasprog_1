U = int(input())
M = int(input())
K = int(input())

minion_beku = M//2
knight_beku = K//2
raja_iblis = 100

Gerebang_1 = U - (knight_beku*2)
Gerebang_2 = Gerebang_1 - ((minion_beku*5))*5
Gerebang_3 = Gerebang_2 - (raja_iblis * 10)

if Gerebang_3 > 0:
    print(f"Yey! Ucup Menang! HP tersisa: {Gerebang_3}")

else:
    print("Yah! Ucup Meninggoy.")