class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer

q1=Question("en ii programlama dili ? ",["c#","python"],"python")

print(q1.checkAnswer("python"))
print(q1.checkAnswer("c#"))