from flask import Flask, render_template, request, redirect
import base64
from io import BytesIO
from PIL import Image
import face_recognition


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detect_faces_in_image(file_stream):
    img = face_recognition.load_image_file(file_stream)
    faces = face_recognition.face_locations(img)
    result = []
    for i in range(len(faces)):
        top, right, bottom, left = faces[i]

        faceImage = img[top:bottom, left:right]
        final = Image.fromarray(faceImage)
        buffered = BytesIO()
        final.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        result.append(img_str)
    return result

@app.route('/')
def hello():
    return {"hello": "world"}

# @app.route("/face-recognition", methods=["POST"])
# def face_recognition():
#     img = request.form.get("img")



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
            return detect_faces_in_image(file)

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

@app.route("/xx")
def xx():
    return {"qq":"xx"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
