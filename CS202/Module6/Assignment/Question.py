class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, answer):
        self.question = question
        self.answers = [answer1, answer2, answer3, answer4]
        self.answer = answer
    
    def getAnswers(self):
        return self.answers
    
    def getAnswer(self):
        return self.answer

    def getQuestion(self):
        return self.question

