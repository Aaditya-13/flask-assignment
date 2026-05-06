from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Cloud</h1><p>Flask app deployed on Render</p><p>Assignment Completed</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
