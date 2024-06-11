
from Question import Question

def main():
    # The questions with four possible answers, only 1 can be correct
    questions = [
        Question("What is the largest mammal?", "Elephant", "Blue Whale", "Great White Shark", "Giraffe", 2),
        Question("What element does 'O' represent on the periodic table?", "Oxygen", "Osmium", "Oganesson", "Osmium", 1),
        Question("Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3),
        Question("What is the capital of Japan?", "Seoul", "Beijing", "Bangkok", "Tokyo", 4),
        Question("Which planet is closest to the sun?", "Earth", "Venus", "Mercury", "Mars", 3),
        Question("What year did the Titanic sink?", "1912", "1905", "1918", "1923", 1),
        Question("What is the smallest country in the world?", "Monaco", "Vatican City", "San Marino", "Liechtenstein", 2),
        Question("Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain", 1),
        Question("What is the chemical formula for water?", "H2O", "CO2", "NaCl", "O2", 1),
        Question("Who discovered penicillin?", "Marie Curie", "Alexander Fleming", "Isaac Newton", "Louis Pasteur", 2)
    ]

    player1_score = 0
    player2_score = 0

    # Questions for the first player
    print("Player 1, it's your turn now, think carefully.")
    for i in range(5):

        print(f"Question {i + 1}: {questions[i].getQuestion()}")
        for j, answer in enumerate(questions[i].getAnswers()):
            print(f"{j + 1}. {answer}")

        response = int(input("Your choice (pick from 1 to 4): "))
        if response == questions[i].getAnswer():
            player1_score += 1
    
    # Questions for the second player
    print("\nPlayer 2, it's your turn now, think carefully.")
    for i in range(5, 10):

        print(f"Question {i - 4}: {questions[i].getQuestion()}")
        for j, answer in enumerate(questions[i].getAnswers()):
            print(f"{j + 1}. {answer}")

        response = int(input("Your choice (pick from 1 to 4): "))
        if response == questions[i].getAnswer():
            player2_score += 1
    
    # displays the players' scores and the winner

    if player1_score > player2_score:
        print("\nPlayer 1 wins!")
    elif player2_score > player1_score:
        print("\nPlayer 2 wins!")
    else:
        print("\nThis game has came to a draw.")


    print("\nScores:")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")
    

if __name__ == "__main__":
    main()
