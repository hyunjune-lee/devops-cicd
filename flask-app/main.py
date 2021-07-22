# third-party imports
import pymysql
from flask import jsonify, render_template, request, redirect

# local imports
from app import app
from models import Results

# from db_config import mysql
from datetime import datetime

# route
@app.route("/")
def index_page():
    # daily_quizs = get_daily_quizs()
    # return render_template("index.html", quizs=daily_quizs)
    return render_template("index.html")


# def get_daily_quizs():
#     daily_quizs = list()
#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         sql = "SELECT * FROM quiz WHERE {0} = DATE_FORMAT(quiz_review_date, '%Y%m%d')".format(
#             datetime.today().strftime("%Y%m%d")
#         )
#         cursor.execute(sql)
#         daily_quizs = cursor.fetchall()
#         # res = jsonify(rows)
#         # res.state_code = 200
#         # return res
#         # table = Results(rows)
#         # table.border = True
#         # return render_template('users.html', table=table)
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()
#         return daily_quizs


# @app.route("/quiz", methods=["GET"])
# def quizs():
#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT * FROM quiz")
#         rows = cursor.fetchall()
#         res = jsonify(rows)
#         res.state_code = 200
#         return res
#         # table = Results(rows)
#         # table.border = True
#         # return render_template('users.html', table=table)
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.route("/quiz/<select_date>", methods=["GET"])
# def quizs_by_date(select_date: str):
#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         sql = "SELECT * FROM quiz WHERE {0} = DATE_FORMAT(quiz_review_date, '%Y%m%d')".format(select_date)
#         cursor.execute(sql)
#         rows = cursor.fetchall()
#         res = jsonify(rows)
#         res.state_code = 200
#         return res
#         # table = Results(rows)
#         # table.border = True
#         # return render_template('users.html', table=table)
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.route("/add", methods=["POST"])
# def add_quiz():
#     conn = None
#     cursor = None
#     try:
#         if request.is_json:
#             req = request.get_json()
#             _question = req["question"]
#             _answer = req["answer"]
#         if _question and _answer and request.method == "POST":
#             sql = "INSERT INTO quiz(quiz_question, quiz_answer, quiz_review_date) VALUES(%s, %s, NOW())"
#             data = (
#                 _question,
#                 _answer,
#             )
#             conn = mysql.connect()
#             cursor = conn.cursor()
#             cursor.execute(sql, data)
#             conn.commit()
#             return redirect("/quiz")
#         else:
#             return "Error while adding quiz"
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.route("/delete/<int:id>", methods=["DELETE"])
# def delete_quiz(id):
#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM quiz WHERE quiz_id=%s", (id,))
#         conn.commit()
#         return redirect("/quiz")
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        "status": 404,
        "message": "Not Found: " + request.url,
    }
    res = jsonify(message)
    res.state_code = 404

    return res


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", PORT= 5000)
