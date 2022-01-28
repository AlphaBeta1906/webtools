from flask import Flask,render_template,abort,send_from_directory
from flask_compress import Compress

app = Flask(__name__)
Compress(app)

@app.errorhandler(404)
def _404(e):
    return render_template("index.html")

@app.route("/robot.txt")
def manifest():
    return send_from_directory("static", "robot.txt")
