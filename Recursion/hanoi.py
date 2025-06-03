# Algorithm qui resous le problème de la tour de Haroi
# Il affiche le nombre du disque et la direction ou il faut le mettre

def hanoi_moves(n, left = True):
    if n == 0:
        return 
    
    hanoi_moves(n - 1, not left)
    if left:
        print(n, "left")
    else:
        print(n, "right")
    
    hanoi_moves(n - 1, not left)