import pymysql
from db_config import mysql


def get_today_quizs():
    conn = mysql.get_connection()

    sql = """
        select todo_content, todo_importance
        from todo
        where todo_status = 1
        order by todo_idx desc
    """

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    data_list = []

    for obj in row:
        data_dic = {"todo_content": obj[0], "todo_importance": obj[1]}
        data_list.append(data_dic)

    conn.close

    return data_list
