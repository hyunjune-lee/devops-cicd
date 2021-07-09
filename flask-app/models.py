from flask_table import Table, Col


class Results(Table):
    quiz_id = Col("Id")
    quiz_question = Col("question")
    quiz_answer = Col("answer")
    quiz_review_date = Col("review_date")
