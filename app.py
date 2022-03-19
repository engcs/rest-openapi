from flask import Flask
import db

app = Flask(__name__)

@app.route("/")
def index():
    html = ["<ul>"]
    for username, user in db.users_dict.items():
        html.append(f"<li><a href='/user/{username}'>{user['nome']}</a></li>")
    html.append("</ul>")
    return "\n".join(html)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)