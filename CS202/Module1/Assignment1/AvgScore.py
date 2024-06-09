
def main():
    golf_file = open('CS202/Module1/Assignment1/GolfScores/golf.txt', 'r')

    average_golf_score = 0
    records = 0

    for line in golf_line:
        if not line.strip().isdigit():
            print(f'Player: {line}')
            continue
        print(f'Score: {line}')
        average_golf_score += int(line)
        records += 1
    
    try:
        average_golf_score /= records
    except ZeroDivisionError:
        print('No records found')
    else:
        print(f'The average gold score is: {average_golf_score}')

if __name__ == '__main__':
    main()