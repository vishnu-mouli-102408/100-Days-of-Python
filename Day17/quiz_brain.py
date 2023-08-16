class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_ques(self):
        return self.question_number < len(self.question_list)
    
    def nextQuestion(self):
        current_quesiton = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_quesiton.text}? (True/False): ")
        self.check_answer(user_input, current_quesiton.answer)
      
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You git it Right!")
        else:
            print("Oops! Wrong Answer")
        print(f"The correct answer was {correct_ans}")    
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")