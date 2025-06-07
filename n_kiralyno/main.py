# Feladat: Egy 8x8-as sakktáblára helyezzünk le 8 királynőt, úgy hogy azok
# ne üssék egymást. Írjuk ki az összes megoldást és hogy hány megoldás van.


def is_valid(board):
    # Sorokat nem kell ellenőrizni, mert a lista elemei, különböző sorokat jelölnek
    if len(board) != len(set(board)):
        return False # Vannak olyanok akik oszlopban ütik egymást
    # Átlók ellenőrzése: ha annyi az oszloptávolság, mint a sortávolság, akkor
    # ütik egymást a királynők
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if j - i == board[i] - board[j] or j - i == board[j] - board[i]:
                return False
    return True

counter = 0
n = 9
for a in range(1, n+1):
    for b in range(1,n+1):
        for c in range(1, n+1):
            for d in range(1,n+1):
                for e in range(1, n+1):
                    for f in range(1,n+1):
                        for g in range(1, n+1):
                            for h in range(1,n+1):
                                for i in range(1,n+1):
                                    if is_valid([a,b,c,d,e,f,g,h,i]):
                                        counter += 1
                                        print(a,b,c,d,e,f,g,h,i)
                                        
print("Megoldások száma:", counter)