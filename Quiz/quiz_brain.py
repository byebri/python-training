class QuizBrain:
    def __init__(self, q_list):
        self.c_question = None
        self.ans = True
        self.q_num = 0
        self.q_list = q_list
        self.points = 0

    def next_question(self):
        self.c_question = self.q_list[self.q_num]
        self.q_num += 1
        self.ans = input(f"Q.{self.q_num}: {self.c_question.text} (True/False)").lower()

    def keep_play(self):
        if self.q_num < len(self.q_list):
            return True

    def check_ans(self):
        answer = self.ans
        result = self.c_question.answer.lower()
        if answer == result:
            self.points += 1
            print(f"You got it! Points: {self.points}/12")
        elif (answer == "true" or answer == "false") and (answer != result):
            print(f"Wrong! Points: {self.points}/12")
        else:
            print("undefined")

