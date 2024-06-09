
def isMagicSquare(grid):
    # Check if the grid has 3 rows
    if len(grid) != 3:
        print("Invalid number of rows")
        return False
    for row in grid:
        # Check if each row has 3 columns
        if len(row) != 3:
            print("Invalid number of columns in a row")
            return False
        numbers = set(range(1, 10))
    for row in grid:
        for num in row:
            # Check if each number in the grid is unique and between 1 and 9
            if num not in numbers:
                print("Invalid number:", num)
                return False
            numbers.remove(num)
            targetSum = sum(grid[0])
    for row in grid:
        # Check if the sum of each row is equal to the target sum
        if sum(row) != targetSum:
            print("Row sum doesn't match target sum")
            return False
    for col in range(3):
        # Check if the sum of each column is equal to the target sum
        if sum(row[col] for row in grid) != targetSum:
            print("Column sum doesn't match target sum")
            return False
        # Check if the sum of the main diagonal is equal to the target sum
        if sum(grid[i][i] for i in range(3)) != targetSum:
            print("Main diagonal sum doesn't match target sum")
            return False
        # Check if the sum of the secondary diagonal is equal to the target sum
        if sum(grid[i][2-i] for i in range(3)) != targetSum:
            print("Secondary diagonal sum doesn't match target sum")
            return False
    return True
def main():
    grid = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    if isMagicSquare(grid):
        print("The grid is a Lo Shu Magic Square")
    else:
        print("The grid isn't Lo Shu Magic Square")
if __name__ == "__main__":
    main()