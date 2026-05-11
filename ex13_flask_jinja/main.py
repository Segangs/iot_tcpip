# ex13_flask_jinja 폴더
# L main.py
# L  static/
#           CSS/style.css
#           JS/script.js
#           images/logo.png
#  templates/
#       base.html
#       index.html


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # 명칭 : 파이썬 : 딕셔너리, 데이터/웹 : json
    user_info = {"username": "iot반", "level": "bootcamp"}
    # 파이썬: 리스트, C/java : 배열
    items = ["Flask 배우기", "jinja 이해", "예쁜 웹앱 만들기"]
    return render_template("index.html", user=user_info, tasks=items)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
