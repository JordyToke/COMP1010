from flask import Flask, request
from pyhtml import html, head, title, body, title, p, form, label, input_, link, h1, header
import requests


# calculate function
def calculate(x, y, symbol):
  if symbol == '+':
    calculate = x + y
  if symbol == '-':
    calculate = x - y
  if symbol == '*':
    calculate = x * y
  if symbol == '/':
    calculate = x / y
  return calculate

app = Flask(__name__, static_folder='static')

@app.route('/', methods=["POST", "GET"])
def hello():
    code = html(
        head(
            title("calculate web server"),
            link(rel="stylesheet", href="../static/calculate_style.css" )
        ),
        body(
            h1("Please enter your text and submit"),
            form(action="result")
            (
                label("First number: "),
                input_(type="number", name="num1", value="0"),
                label("Symbol: "),
                input_(type="text", name="symbol", value="+"),
                label("Second number: "),
                input_(type="number", name="num2", value="0"),
                input_(type="Submit", value="Submit")
            )
        )
    )
    return str(code)

@app.route('/result', methods=["POST", "GET"])
def result():

    #print request.form
    print(f"{request.form=}")
    x = float(request.form['num1'])
    y = float(request.form['num2'])
    symbol = request.form['symbol']

    answer = calculate(x, y, symbol)
    
    code = html(
        head(
            title("Result"),
            link(rel="stylesheet", href="../static/calculate_style.css" )
        ),
        body(
            h1("Please enter your text and submit"),
            form(action="result")
            (
                label("First number: "),
                input_(type="number", name="num1", value="0"),
                label("Symbol: "),
                input_(type="text", name="symbol", value="+"),
                label("Second number: "),
                input_(type="number", name="num2", value="0"),
                input_(type="Submit", value="Submit")
            ),
            p(f"{x} {symbol} {y} = {answer}"),
            form(action="result")
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)