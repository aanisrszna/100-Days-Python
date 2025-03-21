from tokenize import cookie_re


class QuizBrain:
    def __init__(self, q_list):
        self.num = 0
        self.score =0
        self.question_list =q_list

    def still_has_questions(self):
        if self.num < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        current_question = self.question_list[self.num]
        self.num +=1
        user_answer = input(f"Q.{self.num}:{current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer (self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You got it right!")
        else:
            print("That's Wrong")
        print(f"The Correct Answer was: {correct_answer}.")
        print(f"Your Current score is: {self.score}/{self.num}")
        print("\n")

    def last_score(self):
        last_score = f"{self.score}/{self.num}"
