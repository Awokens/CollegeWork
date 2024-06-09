
def main():
    
    player_name = input('Enter player name: ')
    player_score = int(input('Enter player score: '))

    try:
        golf_file = open('CS202/Module1/Assignment1/GolfScores/golf.txt', 'r')

        name = golf_file.readline()
        score = golf_file.readline()
        golf_file.close()

        print(f'Player name: ${name}')
        print(f'Player score: ${score}')

        golf_file.open('CS202/Module1/Assignment1/GolfScores/golf.txt', 'a')
        
        golf_file.write(player_name + '\n')
        golf_file.write(player_score + '\n')

        golf_file.close()

        print('Player name and score appended to golf text file')
    except FileNotFoundError:
        print('File not found')
        print('Creating new file')
        golf_file = open('CS202/Module1/Assignment1/GolfScores/golf.txt', 'w')

        golf_file.write(player_name + '\n')
        golf_file.write(player_score + '\n')
        golf_file.close()

        print('Player name and score written to new golf text file')

if __name__ == '__main__':
    main()
