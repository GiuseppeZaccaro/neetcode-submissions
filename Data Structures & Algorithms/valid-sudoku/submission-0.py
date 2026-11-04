class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        righe = [set() for _ in range(9)]
        colonne = [set() for _ in range(9)]
        quadrati = {(r,c): set() for r in range(3) for c in range(3)}

        for r in range(9):
            for c in range(9):
                valore=board[r][c]

                if valore == ".":
                    continue
                
                if valore in righe[r]:
                    return False
                
                righe[r].add(valore)

                if valore in colonne[c]:
                    return False
                colonne[c].add(valore)

                box_id = (r // 3, c // 3)
                if valore in quadrati[box_id]:
                    return False
                quadrati[box_id].add(valore)
        
        return True