from huggingface_hub import hf_hub_download

REPO_ID = "mT5_multilingual_XLSum"


hf_hub_download(repo_id=REPO_ID, filename=FILENAME)