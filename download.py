import urllib.request, os
from nltk import download

MODEL_PATH = "./save/model-try_1/model.ckpt"
MODEL_URL = "https://www.dropbox.com/s/hyxoj49uw0g4dn8/model.ckpt?dl=1"


def fetch():
    download("punkt")  # Tokenizer
    if not os.path.isfile(MODEL_PATH):
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)