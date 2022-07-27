# 1. serve multiple pages: info page, images page, list + input page
# 2. save inputs into community gardens page

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)