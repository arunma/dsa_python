from typing import *


class NQueens:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.solve_n_queens(n, [], [], [], result)
        print(result)
        ret = []
        for rest in result:
            one_set = []
            for c in rest:
                st = ('.' * c) + 'Q' + '.' * (n - c - 1)
                one_set.append(st)
            ret.append(one_set)
        return ret

    def solve_n_queens(self, n, placements, diag, anti_diag, result):
        r = len(placements)
        if n == r:
            result.append(placements.copy())
            return

        for c in range(n):
            if r + c not in diag and r - c not in anti_diag and c not in placements:
                self.solve_n_queens(n, placements + [c], diag + [r + c], anti_diag + [r - c], result)


if __name__ == '__main__':
    init = NQueens()
    print(init.solveNQueens(4))  # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    # print(init.solveNQueens(1))  # [["Q"]]
