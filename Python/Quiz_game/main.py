from data import question_data
from question_model import Question


question_bank = []
for question in question_data:
    question_text = question["text"]
    answer_text = question["answer"]
    new_question = Question(question_text,answer_text)
    print(new_question)
    question_bank.append(new_question)

print(question_bank)