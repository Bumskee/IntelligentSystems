import math

class Solution:
    def findBestMove(self, board):
        tup = self.minimax(True, board, 1)[1]
        return str(tup[0]), str(tup[1])

    def minimax(self, is_max, board, depth):
        score = self.evaluate(board)
        moves = self.getMoves(board)
        if len(moves) == 0 or score != 0:
            return 0 if score == 0 else score - (depth if is_max else -1 * depth), None

        if is_max:
            best_val = -math.inf
            best_move = None
            for move in moves:
                new_board = [[r[0], r[1], r[2]] for r in board]
                new_board[move[0]][move[1]] = 'x'
                val, _ = self.minimax(False, new_board, depth + 1)
                if val > best_val:
                    best_val = val
                    best_move = move
            return best_val, best_move

        else:
            best_val = math.inf
            best_move = None
            for move in moves:
                new_board = [[r[0], r[1], r[2]] for r in board]
                new_board[move[0]][move[1]] = 'o'
                val, _ = self.minimax(True, new_board, depth + 1)
                if val < best_val:
                    best_val = val
                    best_move = move
            return best_val, best_move

    def getMoves(self, board):
        moves = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    moves.append((row, col))
        return moves

    def evaluate(self, b):
        for i in range(3):
            if b[i][0] != '_' and b[i][0] == b[i][1] and b[i][0] == b[i][2]:
                return -10 if b[i][0] == 'o' else 10
            if b[0][i] != '_' and b[0][i] == b[1][i] and b[0][i] == b[2][i]:
                return -10 if b[0][i] == 'o' else 10
        if b[0][0] != '_' and b[0][0] == b[1][1] and b[0][0] == b[2][2]:
            return -10 if b[0][0] == 'o' else 10
        if b[0][2] != '_' and b[0][2] == b[1][1] and b[0][2] == b[2][0]:
            return -10 if b[0][0] == 'o' else 10
        return 0    # code here


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        board = [['.']*3 for x in range(3)]
        for i in range(3):
            a = input().split()
            for j in range(3):
                board[i][j] = a[j][0]
        
        ob = Solution()
        ans = ob.findBestMove(board)
        print(ans[0] + " " + ans[1])