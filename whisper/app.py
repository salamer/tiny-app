from flask import Flask, render_template, request, redirect
import base64
from whisper_jax import FlaxWhisperPipline
import jax.numpy as jnp

# instantiate pipeline in bfloat16
pipeline = FlaxWhisperPipline("openai/whisper-medium", dtype=jnp.bfloat16)


ALLOWED_EXTENSIONS = {'wav', 'mp3'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route("/xx")
def xx():
    return {"qq":"xx"}


def handle_audio(file_stream):
    text = pipeline(file_stream)
    return text

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return handle_audio(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
