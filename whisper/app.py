from flask import Flask, render_template, request, redirect
import base64
from whisper_jax import FlaxWhisperPipline
import jax.numpy as jnp

# instantiate pipeline in bfloat16
pipeline = FlaxWhisperPipline("openai/whisper-large-v2", dtype=jnp.bfloat16)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route("/xx")
def xx():
    return {"qq":"xx"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
