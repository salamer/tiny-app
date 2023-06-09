from whisper_jax import FlaxWhisperPipline
# instantiate pipeline in bfloat16
pipeline = FlaxWhisperPipline("openai/whisper-medium")