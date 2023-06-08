from flask import Flask, render_template, request, redirect
import base64
from transformers import pipeline

classifier = pipeline("summarization")


app = Flask(__name__)

@app.route("/xx")
def xx():
    return {"qq":"xx"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
