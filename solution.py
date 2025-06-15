class Solution(object):
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = ord(board[i][j]) - ord('1')
                    mask = 1 << d
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i//3)*3 + j//3] |= mask
                else:
                    empties.append((i, j))
        def dfs(k=0):
            if k == len(empties):
                return True
            min_idx, min_count = k, 10
            for idx in range(k, len(empties)):
                i, j = empties[idx]
                used = rows[i] | cols[j] | boxes[(i//3)*3 + j//3]
                count = 9 - bin(used).count('1')
                if count < min_count:
                    min_count, min_idx = count, idx
                    if count == 1:
                        break
            empties[k], empties[min_idx] = empties[min_idx], empties[k]
            i, j = empties[k]
            b = (i//3)*3 + j//3
            used = rows[i] | cols[j] | boxes[b]
            avail = (~used) & 0x1FF
            while avail:
                p = avail & -avail
                avail -= p
                d = p.bit_length() - 1
                board[i][j] = chr(d + ord('1'))
                rows[i] |= p; cols[j] |= p; boxes[b] |= p
                if dfs(k+1):
                    return True
                rows[i] ^= p; cols[j] ^= p; boxes[b] ^= p
                board[i][j] = '.'
            empties[k], empties[min_idx] = empties[min_idx], empties[k]
            return False
        dfs()
