import math

# () -> (7) -> (7,4) -> (7,4,2) -> (7,4,2,8) -> ... (7,4,2,8,6,1,3,5)
def is_valid(board):
    for i in range(len(board) - 1):
        if math.fabs(board[i] - board[-1]) == math.fabs(i - (len(board)-1)):
            return False
    return True

n = 1
while True:
    start_node = tuple() # 1 királynő sincs a táblán

    open_list = [start_node]

    results = []
    

    while len(open_list) > 0:
        current_node = open_list.pop(0)
        if len(current_node) == n:
            results.append(current_node)
        else:
            for i in range(1, n+1):
                if i not in current_node:
                    # Ezen a ponton, tuti fix, hogy nincs 2 királynő egy oszlopban
                    new_node = tuple(list(current_node) + [i])
                    if is_valid(new_node):
                        open_list.append(new_node)

    with open(f"n_kiralyno/megoldasok/{n}_queens.txt", "w", encoding="utf-8") as f:
        f.write(str(len(results)))
        f.write("\n")
        for item in results:
            f.write(str(item))
            f.write("\n")
    n += 1