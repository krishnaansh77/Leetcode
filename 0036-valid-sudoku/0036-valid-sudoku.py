class Solution:
    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                value = board[i][j]

                if value == ".":
                    continue

                # Check row
                if value in rows[i]:
                    return False
                rows[i].add(value)

                # Check column
                if value in columns[j]:
                    return False
                columns[j].add(value)

                # Find box number
                box_number = (i // 3) * 3 + (j // 3)

                # Check box
                if value in boxes[box_number]:
                    return False
                boxes[box_number].add(value)

        return True