from flask import Flask, request
from pyhtml import html, head, title, body, img, p
from PIL import Image
import requests

app = Flask(__name__)

@app.route('/')

def home():
    response = requests.get("https://aws.random.cat/meow")
    img_url = response.json()
    cat_image = img_url["file"]
    fact_response = requests.get("https://catfact.ninja/fact")
    fact_url = fact_response.json()
    fact = fact_url["fact"]

    code = html(
        head(
            title("cat facts")
        ),
        body(
                img(src=cat_image, height=400),
                p(f"{fact}")
            )
        )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)