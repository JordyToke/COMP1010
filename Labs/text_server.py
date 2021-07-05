import string
from flask import Flask, request
from pyhtml import html, head, title, body, title, p, table, tr, td, form, label, input_, strong

app = Flask(__name__)

@app.route('/')
def hello():
    code = html(
        head(
            title("string analysis")
        ),
        body(
            p("Please enter your text and submit"),
            form(action="analysis")
            (
                label("String: "),
                input_(type="text", name="string"),
                input_(type="Submit", value="analyse")
            )
        )
    )
    return str(code)

@app.route('/analysis', methods=["POST"])
def analysis():

    #print request.form
    print(f"{request.form=}")
    text = request.form['string']

    total_length = len(text)
    char_length = 0
    for char in text:
        if char not in string.punctuation:
            char_length += 1
    
    words = len(text.split())

    code = html(
        head(
            title("string analysis")
        ),
        body(
            p("Returned string analysis"),
            table(style="width:400px")(
                tr(
                    td(strong("Total chars:")),
                    td(strong("Chars minus punctuation:")),
                    td(strong("Words:"))
                ),
                tr(
                    td(f"{total_length}"),
                    td(f"{char_length}"),
                    td(f"{words}")
                )
            )
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)