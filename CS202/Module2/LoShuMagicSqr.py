def isMagicSquare(grid):
    # Check if the grid has 3 rows
    if len(grid) != 3:
        print("Invalid number of rows")
        return False
    
    # Check if each row has 3 columns and contains unique numbers between 1 and 9
    uniqueNumbers = [False] * 10  # to track numbers from 1 to 9
    for row in grid:
        if len(row) != 3:
            print("Invalid number of columns in a row")
            return False
        for num in row:
            if num < 1 or num > 9 or uniqueNumbers[num]:
                print("Invalid number:", num)
                return False
            uniqueNumbers[num] = True
    
    # Calculate the target sum using the first row
    targetSum = 0
    for num in grid[0]:
        targetSum += num
    
    # Check if the sum of each row is equal to the target sum
    for row in grid:
        rowSum = 0
        for num in row:
            rowSum += num
        if rowSum != targetSum:
            print("Row sum doesn't match target sum")
            return False
    
    # Check if the sum of each column is equal to the target sum
    for col in range(3):
        colSum = 0
        for row in grid:
            colSum += row[col]
        if colSum != targetSum:
            print("Column sum doesn't match target sum")
            return False
    
    # Check if the sum of the main diagonal is equal to the target sum
    mainDiagSum = 0
    for i in range(3):
        mainDiagSum += grid[i][i]
    if mainDiagSum != targetSum:
        print("Main diagonal sum doesn't match target sum")
        return False
    
    # Check if the sum of the secondary diagonal is equal to the target sum
    secDiagSum = 0
    for i in range(3):
        secDiagSum += grid[i][2 - i]
    if secDiagSum != targetSum:
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
